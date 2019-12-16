from django.shortcuts import render, redirect
import copy
from measuredfood.forms import (
    FullDayOfEatingForm,
    SpecificIngredientFormset,
    SpecificNutrientTargetFormset
    )
from measuredfood.models import (
    RawIngredient3,
    NutrientProfile,
    SpecificNutrientTarget,
)
from measuredfood.models import FullDayOfEating, SpecificIngredient
from django.urls import reverse_lazy
# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from measuredfood.utils.calculate_fulldayofeating\
    import calculate_fulldayofeating
from django.contrib.auth.decorators import login_required
from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
)
import numpy as np

from measuredfood.utils.check_if_author import check_if_author

from measuredfood.utils.save_fulldayofeating_calculation_result_to_database \
    import save_fulldayofeating_calculation_result_to_database

from measuredfood.utils.calculate_total_nutrition_fulldayofeating \
    import calculate_total_nutrition_fulldayofeating

from measuredfood.utils.calculate_percentage_of_target_amount\
    import calculate_percentage_of_target_amount

from measuredfood.utils.set_to_zero_if_none\
    import set_to_zero_if_none

# from measuredfood.utils.judge_total_nutrition\
#     import judge_total_nutrition

from measuredfood.utils.query.query_ingredients_fulldayofeating\
    import query_ingredients_fulldayofeating

from measuredfood.utils.calculate_total_price_fulldayofeating\
    import calculate_total_price_fulldayofeating

from measuredfood.utils.query.query_nutrientprofile_of_fulldayofeating\
    import query_nutrientprofile_of_fulldayofeating

from measuredfood.utils.undo_calculate_average_of_specificingredient_group\
    import undo_calculate_average_of_specificingredient_group

from measuredfood.utils.calculate_average_of_specificingredient_group \
    import calculate_average_of_specificingredient_group

from measuredfood.utils.fulldayofeating.\
    query_input_and_calculate_fulldayofeating\
    import query_input_and_calculate_fulldayofeating

from measuredfood.utils.query.query_result_calculation_fulldayofeating \
    import query_result_calculation_fulldayofeating

from measuredfood.utils.query.query_specificnutrienttarget_of_fulldayofeating\
    import query_specificnutrienttarget_of_fulldayofeating

from measuredfood.utils.fulldayofeating.calculate_percent_max_fulldayofeating \
    import calculate_percent_max_fulldayofeating

from measuredfood.utils.judge_total_nutrition import \
    judge_total_nutrition

from measuredfood.utils.error.custom_error import (
    UserIsNotAuthorError,
    NoSpecificIngredientInFullDayOfEatingError,
    NoValueForTargetedNutrientError,
    NumberTargetedNutrientsNotEqualNumberScalingEntitiesError,
    CalculationResultIsNegativeError,
    FixedIngredientExceedsNutrientProfileValueError,
)


@login_required
def create_fulldayofeating_view(request):
    """
    Largely copied from the update_fulldayofeating function. Always edit that
    function first and copy the changes to the create_fulldayofeating function.
    """

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(
            request.user.id, request.POST
        )
        if form_fulldayofeating.is_valid():
            form_fulldayofeating.instance.author = request.user
            new_fulldayofeating = form_fulldayofeating.save()
            return redirect(
                'update-fulldayofeating',
                id_fulldayofeating=new_fulldayofeating.id
            )
    else:
        form_fulldayofeating = FullDayOfEatingForm(request.user.id)
        context = {'form_fulldayofeating': form_fulldayofeating}
        return render(
            request,
            'measuredfood/fulldayofeating_create.html',
            context
            )


@login_required
def update_fulldayofeating_view(request, id_fulldayofeating):

    try:

        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating,
            id_fulldayofeating,
            UserIsNotAuthorError
            )

        fulldayofeating_object = FullDayOfEating.objects.get(
            pk=id_fulldayofeating
        )

        if request.method == 'POST':
            form_fulldayofeating = FullDayOfEatingForm(
                request.user.id,
                request.POST,
                instance=fulldayofeating_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient = SpecificIngredientFormset(
                request.POST,
                instance=fulldayofeating_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient:
                form.fields['rawingredient'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            formset_specificnutrienttarget = SpecificNutrientTargetFormset(
                request.POST,
                instance=fulldayofeating_object,
            )

            if formset_specificingredient.is_valid() \
                    and form_fulldayofeating.is_valid()\
                    and formset_specificnutrienttarget.is_valid():

                formset_specificingredient.save()
                form_fulldayofeating.save()
                formset_specificnutrienttarget.save()

                return redirect(
                    'update-fulldayofeating',
                    id_fulldayofeating=fulldayofeating_object.id
                    )

            else:
                context = {}
                return render(
                    request,
                    'measuredfood/error/form_fulldayofeating_not_valid.html',
                    context)
        else:
            form_fulldayofeating = FullDayOfEatingForm(
                request.user.id,
                instance=fulldayofeating_object
                )
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient = SpecificIngredientFormset(
                instance=fulldayofeating_object
                )

            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient:
                form.fields['rawingredient'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            formset_specificnutrienttarget = SpecificNutrientTargetFormset(
                instance=fulldayofeating_object,
            )

            context = {
                'formset_specificingredient': formset_specificingredient,
                'form_fulldayofeating': form_fulldayofeating,
                'id_fulldayofeating': id_fulldayofeating,
                'formset_specificnutrienttarget':
                    formset_specificnutrienttarget,
                }
            return render(request, 'measuredfood/fulldayofeating_form.html',
                          context)

    except UserIsNotAuthorError:
        """
        Careful when you implement this. You will have to make changes at 
        multiple spots in the code.
        """
        context = {
            'error_message': 'It seems like you are trying to edit an object '
                             'of another user, which is forbidden.',
            'error_id': 'UserIsNotAuthorError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )


class ListFullDayOfEating(
    LoginRequiredMixin,
    ListView
):
    model = FullDayOfEating

    def get_queryset(self):
        return FullDayOfEating.objects.filter(
            author=self.request.user
        ).order_by('name')


# TODO: Check if the detail views can be deleted.
class DetailFullDayOfEating(UserPassesTestMixin, DetailView):
    model = FullDayOfEating

    def test_func(self):
        fulldayofeating_ = self.get_object()
        if self.request.user == fulldayofeating_.author:
            return True
        return False


class DeleteFullDayOfEating(UserPassesTestMixin, DeleteView):
    model = FullDayOfEating
    success_url = reverse_lazy('list-fulldayofeating')

    def test_func(self):
        fulldayofeating_ = self.get_object()
        if self.request.user == fulldayofeating_.author:
            return True
        return False


@login_required
def calculate_fulldayofeating_view(request, id_fulldayofeating):

    try:
        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating,
            id_fulldayofeating,
            UserIsNotAuthorError,
            )

        fulldayofeating_object = FullDayOfEating.objects.get(
            pk=id_fulldayofeating
        )

        # Copy this function call as is into the mealplan view.
        result_calculate_fulldayofeating,\
            specificingredient_dict_list,\
            nutrientprofile_dict = \
            query_input_and_calculate_fulldayofeating(
                query_ingredients_fulldayofeating,
                query_nutrientprofile_of_fulldayofeating,
                query_specificnutrienttarget_of_fulldayofeating,
                calculate_fulldayofeating,
                calculate_average_of_specificingredient_group,
                undo_calculate_average_of_specificingredient_group,
                save_fulldayofeating_calculation_result_to_database,
                set_to_zero_if_none,
                id_fulldayofeating,
                SpecificIngredient,
                RawIngredient3,
                FullDayOfEating,
                NutrientProfile,
                SpecificNutrientTarget,
                copy,
                ALL_NUTRIENTS_AND_DEFAULT_UNITS,
                np,
                NoSpecificIngredientInFullDayOfEatingError,
                NoValueForTargetedNutrientError,
                NumberTargetedNutrientsNotEqualNumberScalingEntitiesError,
                CalculationResultIsNegativeError,
                FixedIngredientExceedsNutrientProfileValueError,
            )

        result_calculate_fulldayofeating_formatted_for_template = \
            query_result_calculation_fulldayofeating(
                id_fulldayofeating,
                SpecificIngredient,
                RawIngredient3,
                )

        # Calculate the total nutrition of the full day of eating
        result_total_nutrition_fulldayofeating,\
            result_total_nutrition_fulldayofeating_rounded =\
            calculate_total_nutrition_fulldayofeating(
                specificingredient_dict_list,
                ALL_NUTRIENTS_AND_DEFAULT_UNITS,
                set_to_zero_if_none,
            )

        # Make the result_total_nutrition_fulldayofeating_rounded into a list.
        result_total_nutrition_fulldayofeating_rounded_list = []
        nutrient_name_list = []
        for key, value in \
                result_total_nutrition_fulldayofeating_rounded.items():
            result_total_nutrition_fulldayofeating_rounded_list.append(value)
            nutrient_name_list.append(key)

        # Calculate the ratio of the total nutrition in the full day of eating
        # in relation to the target amounts in the nutrient profile and
        # express the result as a percentage.

        nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
            id_fulldayofeating,
            FullDayOfEating,
            NutrientProfile,
        )

        result_percentage_of_target_amount_str,\
            result_percentage_of_target_amount_numbers = \
            calculate_percentage_of_target_amount(
                nutrientprofile_dict,
                result_total_nutrition_fulldayofeating,
                set_to_zero_if_none,
            )

        # Make the result_percentage_of_target_amount_str into a list
        result_percentage_of_target_amount_list = []
        for key, value in result_percentage_of_target_amount_str.items():
            result_percentage_of_target_amount_list.append(value)

        # Make the result_percentage_of_target_amount_numbers into a list
        result_percentage_of_target_amount_numbers_list = []
        for key, value in result_percentage_of_target_amount_numbers.items():
            result_percentage_of_target_amount_numbers_list.append(value)

        # 'Max amount' and 'tolerable upper intake' are used interchangeably.
        result_percent_max_dict, \
            result_percentage_of_tolerable_upper_intake_str_list, \
            result_percentage_of_tolerable_upper_intake_numbers_list = \
            calculate_percent_max_fulldayofeating(
                nutrientprofile_dict,
                result_total_nutrition_fulldayofeating,
            )

        # Make the default units into a list and display them in the table.
        default_unit_list = []
        for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
            default_unit_list.append(dict_k['default_unit'])

        result_judge_total_nutrition, \
            result_judge_total_nutrition_css_class_name = judge_total_nutrition(
                result_percentage_of_target_amount_numbers_list,
                result_percentage_of_tolerable_upper_intake_numbers_list,
                set_to_zero_if_none,
            )

        aggregated_total_nutrition_fulldayofeating = \
            zip(
                nutrient_name_list,
                result_total_nutrition_fulldayofeating_rounded_list,
                default_unit_list,
                result_percentage_of_target_amount_list,
                result_percentage_of_tolerable_upper_intake_str_list,
                result_judge_total_nutrition,
                result_judge_total_nutrition_css_class_name,
                )

        total_price_fulldayofeating_result_dict = \
            calculate_total_price_fulldayofeating(
                specificingredient_dict_list
            )

        context = {'id_fulldayofeating': id_fulldayofeating,
                   'result_calculate_fulldayofeating_formatted_for_template':
                   result_calculate_fulldayofeating_formatted_for_template,
                   'result_calculate_fulldayofeating':
                   result_calculate_fulldayofeating,
                   'aggregated_total_nutrition_fulldayofeating':
                   aggregated_total_nutrition_fulldayofeating,
                   'result_percentage_of_target_amount':
                   result_percentage_of_target_amount_str,
                   'total_price_fulldayofeating_result_dict':
                   total_price_fulldayofeating_result_dict,
                   'fulldayofeating_object': fulldayofeating_object,
                   }

        return render(
            request,
            'measuredfood/fulldayofeating_calculation_result.html',
            context
            )

    except NoSpecificIngredientInFullDayOfEatingError:
        context = {
            'error_message': 'Please add at least one ingredient to your full '
                             'day of eating before calculating the full day '
                             'of eating.',
            'error_id': 'NoSpecificIngredientInFullDayOfEatingError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )

    except UserIsNotAuthorError:
        """
        Careful when you implement this. You will have to make changes at 
        multiple spots in the code.
        """
        context = {
            'error_message': 'It seems like you are trying to edit an object '
                             'of another user, which is forbidden.',
            'error_id': 'UserIsNotAuthorError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )

    except NoValueForTargetedNutrientError as e:
        list_ = e.nutrient_value_missing
        seperator = ', '
        pretty_list = seperator.join(list_)
        error_message = \
            'The values for the following nutrients in the nutrient profile ' \
            'are missing: '\
            + pretty_list\
            + '.'\
            + ' Please add values for these nutrients in the ' \
              'nutrient profile or do not target them.'
        context = {
            'error_message': error_message,
            'error_id': 'NoValueForTargetedNutrientError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )
    except NumberTargetedNutrientsNotEqualNumberScalingEntitiesError as e:

        seperator = ', '
        pretty_list_targeted_nutrient = seperator.join(e.list_targeted_nutrient)
        pretty_list_independently_scaling_entity = \
            seperator.join(e.list_independently_scaling_entity)

        error_message = 'The number of nutrient targets did not match the ' \
                        'number of independently scaling ingredients or ' \
                        'ingredient groups.' \
                        'There were '\
                        + str(e.n_targeted_nutrient) \
                        + ' targeted nutrients: ' \
                        + pretty_list_targeted_nutrient \
                        + '.' \
                        + 'There were '\
                        + str(e.n_independently_scaling_entity) \
                        + ' independently scaling ingredients or ingredient ' \
                          'groups: ' \
                        + pretty_list_independently_scaling_entity \
                        + '.'
        context = {
            'error_message': error_message,
            'error_id':
                'NumberTargetedNutrientsNotEqualNumberScalingEntitiesError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )
    except CalculationResultIsNegativeError as e:
        seperator = ', '
        pretty_list_ingredient_negative_result = seperator.join(
            e.list_ingredient_negative_result
        )

        if len(e.list_ingredient_negative_result) == 1:
            error_message = \
                'The calculation result for the ingredient ' \
                + pretty_list_ingredient_negative_result \
                + ' was negative.' \
                + ' Try setting the scaling options of that ingredient to ' \
                '\'fixed\'. The amount of that ingredient should ' \
                'probably be ' \
                'set to 0. As a consequence, the number of independently ' \
                'scaling ingredients is reduced and therefore, ' \
                  'fewer nutrients ' \
                'must be targeted to maintain equality between the number of ' \
                'targeted nutrients and independently scaling ingredients or ' \
                'ingredient groups.'
        elif len(e.list_ingredient_negative_result > 1):
            error_message = \
                'The calculation results for the ingredients ' \
                + pretty_list_ingredient_negative_result \
                + ' were negative.' \
                + ' Try setting the scaling options of those ingredients to ' \
                '\'fixed\'. The amounts of those ingredients should ' \
                'probably be ' \
                'set to 0. As a consequence, the number of independently ' \
                'scaling ingredients is reduced and therefore, ' \
                  'fewer nutrients ' \
                'must be targeted to maintain equality between the number of ' \
                'targeted nutrients and independently scaling ingredients or ' \
                'ingredient groups.'
        else:
            error_message = None
            print('This case should not be possible.')

        context = {
            'error_message': error_message,
            'error_id':
                'CalculationResultIsNegativeError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )

    except FixedIngredientExceedsNutrientProfileValueError:

        context = {
            'error_message': 'The fixed ingredient exceed the values '
                             'specified for the nutrient profile. For example: '
                             'someone adds 1000 g of bacon to a recipe with '
                             'the scaling option "fixed", adds eggs with a '
                             'scaling option of "independent" and has a fat '
                             'target of 70 g. It is not possible to add a '
                             'positive amount of eggs so that the total fat '
                             'amount gets to 70 g, because the bacon already '
                             'provides more than that.',
            'error_id': 'FixedIngredientExceedsNutrientProfileValueError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )
