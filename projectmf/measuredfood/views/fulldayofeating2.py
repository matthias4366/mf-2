from django.shortcuts import render, redirect
import copy
from measuredfood.forms import (
    FullDayOfEating2Form,
    SpecificIngredient2Formset,
    SpecificNutrientTarget2Formset
    )
from measuredfood.models import (
    RawIngredient3,
    NutrientProfile,
    SpecificNutrientTarget2,
    SpecificIngredient2,
    FullDayOfEating2,
)
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

# from measuredfood.utils.query.query_specificnutrienttarget2_of_fulldayofeating\
#     import query_specificnutrienttarget2_of_fulldayofeating

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
def create_fulldayofeating2_view(request):
    """
    The FullDayOfEating2 has to first be created and saved to the database.
    Afterwards, the SpecificIngredient2 objects can be created; since they
    are related to the FullDayOfEating2 object.
    """

    if request.method == 'POST':
        form_fulldayofeating2 = FullDayOfEating2Form(
            request.user.id, request.POST
        )
        if form_fulldayofeating2.is_valid():
            form_fulldayofeating2.instance.author = request.user
            new_fulldayofeating = form_fulldayofeating2.save()
            return redirect(
                'update-fulldayofeating2',
                id_fulldayofeating2=new_fulldayofeating.id
            )
    else:
        form_fulldayofeating2 = FullDayOfEating2Form(request.user.id)
        context = {'form_fulldayofeating2': form_fulldayofeating2}
        return render(
            request,
            'measuredfood/fulldayofeating2_create.html',
            context
            )


@login_required
def update_fulldayofeating2_view(request, id_fulldayofeating2):

    try:

        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating2,
            id_fulldayofeating2,
            UserIsNotAuthorError
            )

        fulldayofeating2_object = FullDayOfEating2.objects.get(
            pk=id_fulldayofeating2
        )

        if request.method == 'POST':
            form_fulldayofeating2 = FullDayOfEating2Form(
                request.user.id,
                request.POST,
                instance=fulldayofeating2_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # That is because of how the FullDayOfEating2Form is set up.
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating2.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient2 = SpecificIngredient2Formset(
                request.POST,
                instance=fulldayofeating2_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient2:
                form.fields['rawingredient'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            formset_specificnutrienttarget2 = SpecificNutrientTarget2Formset(
                request.POST,
                instance=fulldayofeating2_object,
            )

            if formset_specificingredient2.is_valid() \
                    and form_fulldayofeating2.is_valid()\
                    and formset_specificnutrienttarget2.is_valid():

                formset_specificingredient2.save()
                form_fulldayofeating2.save()
                formset_specificnutrienttarget2.save()

                return redirect(
                    'update-fulldayofeating2',
                    id_fulldayofeating2=fulldayofeating2_object.id
                    )

            else:
                context = {}
                return render(
                    request,
                    'measuredfood/error/form_fulldayofeating_not_valid.html',
                    context)
        else:
            form_fulldayofeating2 = FullDayOfEating2Form(
                request.user.id,
                instance=fulldayofeating2_object
                )
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating2.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient2 = SpecificIngredient2Formset(
                instance=fulldayofeating2_object
                )

            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient2:
                form.fields['rawingredient'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            formset_specificnutrienttarget2 = SpecificNutrientTarget2Formset(
                instance=fulldayofeating2_object,
            )

            context = {
                'formset_specificingredient2': formset_specificingredient2,
                'form_fulldayofeating2': form_fulldayofeating2,
                'id_fulldayofeating2': id_fulldayofeating2,
                'formset_specificnutrienttarget2':
                    formset_specificnutrienttarget2,
                }
            return render(request, 'measuredfood/fulldayofeating2_form.html',
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


class ListFullDayOfEating2(
    LoginRequiredMixin,
    ListView
):
    model = FullDayOfEating2

    def get_queryset(self):
        return FullDayOfEating2.objects.filter(
            author=self.request.user
        ).order_by('name')


# TODO: Adapt this view to FullDayOfEating2
class DetailFullDayOfEating2(DetailView):
    model = FullDayOfEating2

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Access the FullDayOfEating2 object in order to query the correct
        # specificnutrienttarget_queryset.
        id_full_day_of_eating_ = context['object'].id

        specificnutrienttarget_queryset = \
            SpecificNutrientTarget2.objects.filter(
                fulldayofeating=id_full_day_of_eating_
            )
        specificnutrienttarget_list = list(
            specificnutrienttarget_queryset.values('nutrient_target')
        )
        context['specificnutrienttarget_list'] = \
            specificnutrienttarget_list

        specificingredient_queryset = SpecificIngredient2.objects.filter(
            fulldayofeating=id_full_day_of_eating_
        )
        specificingredient_list = list(
            specificingredient_queryset
        )
        context['specificingredient_list'] = \
            specificingredient_list

        return context


class DeleteFullDayOfEating2(UserPassesTestMixin, DeleteView):
    model = FullDayOfEating2
    success_url = reverse_lazy('list-fulldayofeating2')

    def test_func(self):
        fulldayofeating_ = self.get_object()
        if self.request.user == fulldayofeating_.author:
            return True
        return False


# TODO: Adapt this view to FullDayOfEating2
@login_required
def calculate_fulldayofeating2_view(request, id_fulldayofeating2):

    try:
        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating2,
            id_fulldayofeating2,
            UserIsNotAuthorError,
            )

        fulldayofeating2_object = FullDayOfEating2.objects.get(
            pk=id_fulldayofeating2
        )

        query_specificnutrienttarget2_of_fulldayofeating = None

        # Copy this function call as is into the mealplan view.
        result_calculate_fulldayofeating,\
            specificingredient_dict_list,\
            nutrientprofile_dict = \
            query_input_and_calculate_fulldayofeating(
                query_ingredients_fulldayofeating,
                query_nutrientprofile_of_fulldayofeating,
                query_specificnutrienttarget2_of_fulldayofeating,
                calculate_fulldayofeating,
                calculate_average_of_specificingredient_group,
                undo_calculate_average_of_specificingredient_group,
                save_fulldayofeating_calculation_result_to_database,
                set_to_zero_if_none,
                id_fulldayofeating2,
                SpecificIngredient2,
                RawIngredient3,
                FullDayOfEating2,
                NutrientProfile,
                SpecificNutrientTarget2,
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
                id_fulldayofeating2,
                SpecificIngredient2,
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
        nutrient_name_measuredfood_list = []
        for key, value in \
                result_total_nutrition_fulldayofeating_rounded.items():
            result_total_nutrition_fulldayofeating_rounded_list.append(value)
            nutrient_name_measuredfood_list.append(key)

        # Calculate the ratio of the total nutrition in the full day of eating
        # in relation to the target amounts in the nutrient profile and
        # express the result as a percentage.

        nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
            id_fulldayofeating2,
            FullDayOfEating2,
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
            default_unit_list.append(dict_k['unit_nutrient_usda_api'])

        result_judge_total_nutrition, \
            result_judge_total_nutrition_css_class_name = judge_total_nutrition(
                result_percentage_of_target_amount_numbers_list,
                result_percentage_of_tolerable_upper_intake_numbers_list,
                set_to_zero_if_none,
            )

        aggregated_total_nutrition_fulldayofeating = \
            zip(
                nutrient_name_measuredfood_list,
                result_total_nutrition_fulldayofeating_rounded_list,
                default_unit_list,
                result_percentage_of_target_amount_list,
                result_percentage_of_tolerable_upper_intake_str_list,
                result_judge_total_nutrition,
                result_judge_total_nutrition_css_class_name,
                )

        aggregated_ = copy.deepcopy(aggregated_total_nutrition_fulldayofeating)

        # Remove the nutrients which are not to be displayed.
        aggregated_total_nutrition_not_all_nutrients_displayed = []
        for ab in aggregated_:
            for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
                if nutrient_dict['is_displayed']:
                    if ab[0] == nutrient_dict['nutrient_name_measuredfood']:
                        # Add a tuple containing the nutrient name from the
                        # USDA API, which is much more readable and thus
                        # better to display.
                        ab = ab + (nutrient_dict['nutrient_name_usda_api'],)
                        aggregated_total_nutrition_not_all_nutrients_displayed.\
                            append(ab)
                    else:
                        continue
                else:
                    continue

        total_price_fulldayofeating_result_dict = \
            calculate_total_price_fulldayofeating(
                specificingredient_dict_list
            )

        context = {'id_fulldayofeating2': id_fulldayofeating2,
                   'result_calculate_fulldayofeating_formatted_for_template':
                   result_calculate_fulldayofeating_formatted_for_template,
                   'result_calculate_fulldayofeating':
                   result_calculate_fulldayofeating,
                   'aggregated_total_nutrition_fulldayofeating':
                   aggregated_total_nutrition_not_all_nutrients_displayed,
                   # aggregated_total_nutrition_fulldayofeating,
                   'result_percentage_of_target_amount':
                   result_percentage_of_target_amount_str,
                   'total_price_fulldayofeating_result_dict':
                   total_price_fulldayofeating_result_dict,
                   'fulldayofeating2_object': fulldayofeating2_object,
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


# TODO: Adapt this view to FullDayOfEating2
def copy_fulldayofeating2_to_user(request, id_fulldayofeating2):
    """
    From the publicly available full days of eating, copy a full day of
    eating to the user's full day of eating objects.
    :return:
    """

    # Copy the nutrient profile:
    nutrient_profile = FullDayOfEating2.objects.get(
        id=id_fulldayofeating2
    ).nutrient_profile
    nutrient_profile_copy = NutrientProfile.objects.get(
        id=nutrient_profile.id
    )
    nutrient_profile_copy.pk = None
    nutrient_profile_copy.author = request.user
    nutrient_profile_copy.save()

    # Copy the full day of eating, along with the SpecificNutrientTarget2 and
    # the SpecificIngredient2 and the RawIngredient3 objects.
    full_day_of_eating_copy = FullDayOfEating2.objects.get(
        id=id_fulldayofeating2
    )
    full_day_of_eating_copy.pk = None
    full_day_of_eating_copy.author = request.user
    full_day_of_eating_copy.nutrient_profile = nutrient_profile_copy
    full_day_of_eating_copy.save()

    specific_nutrient_target_queryset = SpecificNutrientTarget2.objects.filter(
        fulldayofeating=id_fulldayofeating2
    )
    # Copy all SpecificNutrientTarget2 objects.
    for specific_nutrient_target_k in specific_nutrient_target_queryset:
        specific_nutrient_target_copy_k = specific_nutrient_target_k
        specific_nutrient_target_copy_k.pk = None
        specific_nutrient_target_copy_k.fulldayofeating = \
            full_day_of_eating_copy
        specific_nutrient_target_copy_k.save()

    # Copy all SpecificIngredient2 objects.
    specific_ingredient_queryset = SpecificIngredient2.objects.filter(
        fulldayofeating=id_fulldayofeating2
    )

    for specific_ingredient_k in specific_ingredient_queryset:
        raw_ingredient3_copy = specific_ingredient_k.rawingredient
        raw_ingredient3_copy.pk = None
        raw_ingredient3_copy.author = request.user
        raw_ingredient3_copy.save()
        specific_ingredient_copy = specific_ingredient_k
        specific_ingredient_copy.pk = None
        specific_ingredient_copy.rawingredient = raw_ingredient3_copy
        specific_ingredient_copy.fulldayofeating = full_day_of_eating_copy
        specific_ingredient_copy.save()

    fulldayofeating_list = FullDayOfEating2.objects.filter(
        author=request.user
    ).order_by('name')

    context = {'fulldayofeating_list': fulldayofeating_list}

    return render(
        request,
        'measuredfood/fulldayofeating_list.html',
        context
    )
