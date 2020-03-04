import copy
import json

# imports for the creation of user accounts
from django.shortcuts import render, redirect

# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from measuredfood.models import (
    Mealplan,
    FullDayOfEating,
    SpecificFullDayOfEating,
    SpecificIngredient,
    NutrientProfile,
    RawIngredient3,
    SpecificNutrientTarget,
)
from measuredfood.forms import (
    MealplanForm,
    SpecificFullDayOfEatingFormset
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from measuredfood.utils.check_if_author import check_if_author
import numpy as np

from measuredfood.utils.calculate_fulldayofeating import \
    calculate_fulldayofeating

from measuredfood.utils.save_fulldayofeating_calculation_result_to_database \
    import save_fulldayofeating_calculation_result_to_database

from measuredfood.utils.query.query_ingredients_fulldayofeating\
    import query_ingredients_fulldayofeating

from measuredfood.utils.calculate_total_nutrition_fulldayofeating \
    import calculate_total_nutrition_fulldayofeating

from measuredfood.utils.set_to_zero_if_none\
    import set_to_zero_if_none

from measuredfood.utils.query.query_nutrientprofile_of_fulldayofeating\
    import query_nutrientprofile_of_fulldayofeating

from measuredfood.utils.calculate_percentage_of_target_amount\
    import calculate_percentage_of_target_amount

from measuredfood.utils.query.query_nutrientprofile_of_mealplan\
    import query_nutrientprofile_of_mealplan

from measuredfood.utils.calculate_total_price_fulldayofeating import \
    calculate_total_price_fulldayofeating

from measuredfood.utils.calculate_average_of_specificingredient_group import \
    calculate_average_of_specificingredient_group

from measuredfood.utils.undo_calculate_average_of_specificingredient_group \
    import undo_calculate_average_of_specificingredient_group

from measuredfood.utils.fulldayofeating\
    .query_input_and_calculate_fulldayofeating\
    import query_input_and_calculate_fulldayofeating

from measuredfood.utils.query.query_specificnutrienttarget_of_fulldayofeating \
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

import math

import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')

# /home/matthias/1_local_code/mf-2/projectmf/data/nutrient_dict_list.json

with open('data/nutrient_dict_list.json', 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)


@login_required
def create_mealplan_view(request):
    view_type = 'create'

    if request.method == 'POST':
        form_mealplan = MealplanForm(request.POST)
        if form_mealplan.is_valid():
            form_mealplan.instance.author = request.user
            new_mealplan = form_mealplan.save()
            return redirect(
                'update-mealplan',
                id_mealplan=new_mealplan.id
            )
    else:
        form_mealplan = MealplanForm()
        context = {'form_mealplan': form_mealplan,
                   'view_type': view_type}
        return render(
            request,
            'measuredfood/mealplan_form.html',
            context
            )


@login_required
def update_mealplan_view(request, id_mealplan):

    try:

        view_type = 'update'

        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            Mealplan,
            id_mealplan,
            UserIsNotAuthorError,
            )

        mealplan_object = Mealplan.objects.get(pk=id_mealplan)

        if request.method == 'POST':
            form_mealplan = MealplanForm(
                request.POST,
                instance=mealplan_object
            )
            formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
                request.POST,
                instance=mealplan_object
            )

            if form_mealplan.is_valid() and \
                    formset_specificfulldayofeating.is_valid():
                formset_specificfulldayofeating.save()
                form_mealplan.save()
                return redirect(
                    'update-mealplan',
                    id_mealplan=mealplan_object.id
                    )
        else:
            form_mealplan = MealplanForm(instance=mealplan_object)
            formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
                instance=mealplan_object
            )
            # Only let the user select FullDayOfEating objects from their own
            # collection.
            for form in formset_specificfulldayofeating:
                form.fields['fulldayofeating'].queryset = \
                        FullDayOfEating.objects.filter(
                    author=request.user.id
                )

            context = {
                'form_mealplan': form_mealplan,
                'formset_specificfulldayofeating':
                    formset_specificfulldayofeating,
                'id_mealplan': mealplan_object.id,
                'view_type': view_type
            }
            # TODO: use reverse_lazy instead of hard coding
            #  the name of the html file.
            return render(request, 'measuredfood/mealplan_form.html', context)

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


@login_required
def shoppinglist_view(request, id_mealplan):

    # From id_mealplan, get all the related SpecificFullDayOfEating objects.
    queryset_specificfulldayofeating = SpecificFullDayOfEating.objects.filter(
        mealplan=id_mealplan
    )

    # From all the SpecificFullDayOfEating, get the related FullDayOfEating
    # objects.
    queryset_related_fulldayofeating = \
        queryset_specificfulldayofeating.values('fulldayofeating')
    list_dict_related_fulldayofeating = list(queryset_related_fulldayofeating)

    # Save the id values in a list. Make two lists: one without
    # duplications for the recalculation and one with duplications for the
    # making of the shopping list.
    id_list_no_duplications = []
    id_list_with_duplications = []
    for k in range(len(list_dict_related_fulldayofeating)):
        # A for loop is used for a dictionary that only has one entry.
        for key, value in list_dict_related_fulldayofeating[k].items():
            id_list_with_duplications.append(value)
            if value not in id_list_no_duplications:
                id_list_no_duplications.append(value)

    # Iterate through the id_list_no_duplications and recalculate the amounts
    # for every FullDayOfEating in that list. Write a separate function for
    # that which just takes in the id of the FullDayOfEating and does
    # everything else on its own.
    for k in range(len(id_list_no_duplications)):
        id_fulldayofeating = id_list_no_duplications[k]

        try:

            # Copy the query_input_and_calculate_fulldayofeating from the
            # fulldayofeating.py file exactly as it is.
            result_calculate_fulldayofeating, \
            specificingredient_dict_list, \
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

        except NoSpecificIngredientInFullDayOfEatingError:
            context = {
                'error_message': 'Please add at least one ingredient to your '
                                 'full '
                                 'day of eating before calculating the full '
                                 'day '
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
                'error_message': 'It seems like you are trying to edit an '
                                 'object '
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
                'The values for the following nutrients in the nutrient ' \
                'profile ' \
                'are missing: ' \
                + pretty_list \
                + '.' \
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
            pretty_list_targeted_nutrient = seperator.join(
                e.list_targeted_nutrient)
            pretty_list_independently_scaling_entity = \
                seperator.join(e.list_independently_scaling_entity)

            error_message = 'The number of nutrient targets did not ' \
                            'match the ' \
                            'number of independently ' \
                            'scaling ingredients or ' \
                            'ingredient groups.' \
                            'There were ' \
                            + str(e.n_targeted_nutrient) \
                            + ' targeted nutrients: ' \
                            + pretty_list_targeted_nutrient \
                            + '.' \
                            + 'There were ' \
                            + str(e.n_independently_scaling_entity) \
                            + ' independently scaling ingredients ' \
                              'or ingredient ' \
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
                    + ' Try setting the scaling options of that' \
                      ' ingredient to ' \
                      '\'fixed\'. The amount of that ingredient should ' \
                      'probably be ' \
                      'set to 0. As a consequence, ' \
                      'the number of independently ' \
                      'scaling ingredients is reduced and therefore, ' \
                      'fewer nutrients ' \
                      'must be targeted to maintain ' \
                      'equality between the number of ' \
                      'targeted nutrients and independently ' \
                      'scaling ingredients or ' \
                      'ingredient groups.'
            elif len(e.list_ingredient_negative_result > 1):
                error_message = \
                    'The calculation results for the ingredients ' \
                    + pretty_list_ingredient_negative_result \
                    + ' were negative.' \
                    + ' Try setting the scaling options ' \
                      'of those ingredients to ' \
                      '\'fixed\'. The amounts of those ingredients should ' \
                      'probably be ' \
                      'set to 0. As a consequence, the ' \
                      'number of independently ' \
                      'scaling ingredients is reduced and therefore, ' \
                      'fewer nutrients ' \
                      'must be targeted to maintain ' \
                      'equality between the number of ' \
                      'targeted nutrients and ' \
                      'independently scaling ingredients or ' \
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
                                 'specified for the nutrient profile. '
                                 'For example: '
                                 'someone adds 1000 g of bacon'
                                 ' to a recipe with '
                                 'the scaling option "fixed", adds eggs with a '
                                 'scaling option of "independent"'
                                 ' and has a fat '
                                 'target of 70 g. It is not possible to add a '
                                 'positive amount of eggs '
                                 'so that the total fat '
                                 'amount gets to 70 g, '
                                 'because the bacon already '
                                 'provides more than that.',
                'error_id': 'FixedIngredientExceedsNutrientProfileValueError',
            }
            return render(
                request,
                'measuredfood/error/general_error_page.html',
                context
            )

    shopping_list = {}

    # Iterate over the id_list_with_duplications.
    for id_fulldayofeating_k in id_list_with_duplications:
        queryset_specificingredient_for_sum = SpecificIngredient.objects.filter(
            fulldayofeating=id_fulldayofeating_k
        ).values()
        list_specificingredient_for_sum = \
            list(queryset_specificingredient_for_sum)

        # For each FullDayOfEating in
        # that list, iterate over all the SpecificIngredients.
        for dict_specificingredient_k in list_specificingredient_for_sum:
            # For each SpecificIngredient,
            # get the name of the associated RawIngredient3.
            rawingredient_id = dict_specificingredient_k['rawingredient_id']
            query_rawingredient_name = RawIngredient3.objects.filter(
                id=rawingredient_id
            ).values('name')

            rawingredient_name = list(query_rawingredient_name)[0]['name']

            # New code:
            # Check if the name of the RawIngredient3 is already in the
            # shopping_list.
            # If it is not, add it and initialize the sum total
            # amount as 0.
            if rawingredient_name not in shopping_list:
                new_dict = {
                    rawingredient_name:
                        {
                            'amount': 0,
                            'unit': None,
                        }
                }
                shopping_list.update(new_dict)

            # After that, add the calculated_amount of the SpecificIngredient
            # which is related to the RawIngredient3 to the sum total amount.
            shopping_list[rawingredient_name]['amount'] = \
                shopping_list[rawingredient_name]['amount'] \
                + dict_specificingredient_k['calculated_amount']

            # Add unit.
            shopping_list[rawingredient_name]['unit'] = \
                dict_specificingredient_k['base_amount_unit']

    # Round up the sums in the shopping list.
    for key, value in shopping_list.items():
        value['amount'] = math.ceil(value['amount'])

    context = {
        'results_shopping_list': shopping_list,
        'id_mealplan': id_mealplan,
        }
    return render(request, 'measuredfood/shoppinglist.html', context)


class ListMealplan(
    LoginRequiredMixin,
    ListView
):
    model = Mealplan

    def get_queryset(self):
        return Mealplan.objects.filter(
            author=self.request.user
        ).order_by('name')


class DetailMealplan(DetailView):
    model = Mealplan


class DeleteMealplan(UserPassesTestMixin, DeleteView):
    model = Mealplan
    success_url = reverse_lazy('list-mealplan')

    def test_func(self):
        mealplan = self.get_object()
        if self.request.user == mealplan.author:
            return True
        return False


@login_required
def mealplan_average_nutrition_view(request, id_mealplan):

    # From id_mealplan, get all the related SpecificFullDayOfEating objects.
    queryset_specificfulldayofeating = SpecificFullDayOfEating.objects.filter(
        mealplan=id_mealplan
    )

    # From all the SpecificFullDayOfEating, get the related FullDayOfEating
    # objects.
    queryset_related_fulldayofeating = \
        queryset_specificfulldayofeating.values('fulldayofeating')
    list_dict_related_fulldayofeating = list(queryset_related_fulldayofeating)

    # Save the id values in a list. Make two lists: one without
    # duplications for the recalculation and one with duplications for the
    # making of the shopping list.
    id_list_no_duplications = []
    id_list_with_duplications = []
    for k in range(len(list_dict_related_fulldayofeating)):
        # This seems inefficient and confusing, but is also should not matter.
        for key, value in list_dict_related_fulldayofeating[k].items():
            id_list_with_duplications.append(value)
            if value not in id_list_no_duplications:
                id_list_no_duplications.append(value)

    # Iterate through the id_list_no_duplications and recalculate the amounts
    # for every FullDayOfEating in that list. Write a separate function for
    # that which just takes in the id of the FullDayOfEating and does
    # everything else on its own.
    for k in range(len(id_list_no_duplications)):
        id_fulldayofeating = id_list_no_duplications[k]

        # Copy the query_input_and_calculate_fulldayofeating from the
        # fulldayofeating.py file exactly as it is.

        try:
            result_calculate_fulldayofeating, \
                specificingredient_dict_list, \
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
        except NoSpecificIngredientInFullDayOfEatingError:
            context = {
                'error_message': 'Please add at least one'
                                 ' ingredient to your full '
                                 'day of eating before '
                                 'calculating the full day '
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
                'error_message': 'It seems like you are trying '
                                 'to edit an object '
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
                'The values for the following nutrients ' \
                'in the nutrient profile ' \
                'are missing: ' \
                + pretty_list \
                + '.' \
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
            pretty_list_targeted_nutrient = seperator.join(
                e.list_targeted_nutrient)
            pretty_list_independently_scaling_entity = \
                seperator.join(e.list_independently_scaling_entity)

            error_message = 'The number of nutrient targets ' \
                            'did not match the ' \
                            'number of independently scaling ingredients or ' \
                            'ingredient groups.' \
                            'There were ' \
                            + str(e.n_targeted_nutrient) \
                            + ' targeted nutrients: ' \
                            + pretty_list_targeted_nutrient \
                            + '.' \
                            + 'There were ' \
                            + str(e.n_independently_scaling_entity) \
                            + ' independently scaling ' \
                              'ingredients or ingredient ' \
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
                    + ' Try setting the scaling ' \
                      'options of that ingredient to ' \
                      '\'fixed\'. The amount of that ingredient should ' \
                      'probably be ' \
                      'set to 0. As a consequence, ' \
                      'the number of independently ' \
                      'scaling ingredients is reduced and therefore, ' \
                      'fewer nutrients ' \
                      'must be targeted to maintain ' \
                      'equality between the number of ' \
                      'targeted nutrients and ' \
                      'independently scaling ingredients or ' \
                      'ingredient groups.'
            elif len(e.list_ingredient_negative_result > 1):
                error_message = \
                    'The calculation results for the ingredients ' \
                    + pretty_list_ingredient_negative_result \
                    + ' were negative.' \
                    + ' Try setting the scaling ' \
                      'options of those ingredients to ' \
                      '\'fixed\'. The amounts of those ingredients should ' \
                      'probably be ' \
                      'set to 0. As a consequence, ' \
                      'the number of independently ' \
                      'scaling ingredients is reduced and therefore, ' \
                      'fewer nutrients ' \
                      'must be targeted to maintain ' \
                      'equality between the number of ' \
                      'targeted nutrients and ' \
                      'independently scaling ingredients or ' \
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
                                 'specified for the nutrient profile. '
                                 'For example: '
                                 'someone adds 1000 g of bacon'
                                 ' to a recipe with '
                                 'the scaling option "fixed",'
                                 ' adds eggs with a '
                                 'scaling option of "independent" '
                                 'and has a fat '
                                 'target of 70 g. '
                                 'It is not possible to add a '
                                 'positive amount of eggs '
                                 'so that the total fat '
                                 'amount gets to 70 g, '
                                 'because the bacon already '
                                 'provides more than that.',
                'error_id': 'FixedIngredientExceedsNutrientProfileValueError',
            }
            return render(
                request,
                'measuredfood/error/general_error_page.html',
                context
            )

    # The calculated_amount values for the FullDayOfEating objects have been
    # recalculated. Now to the calculation of the average daily nutrition.

    # Make a list which contains the average nutrition for each full day of
    # eating in the mealplan. This list will later be used to calculate the
    # average.
    result_total_nutrition_fulldayofeating_list = []

    # Gather all the specificingredient_dict_list in a list for the calculation
    # of the average price of the mealplan later. This is done in order to
    # separate out the code as much as possible.
    specificingredient_dict_list_mealplan = []

    # Calculate the nutrition sum for each FullDayOfEating.
    # Iterate over the id_list_with_duplications.
    for id_fulldayofeating in id_list_with_duplications:

        specificingredient_dict_list = query_ingredients_fulldayofeating(
            id_fulldayofeating,
            SpecificIngredient,
            RawIngredient3,
            ALL_NUTRIENTS_AND_DEFAULT_UNITS,
            set_to_zero_if_none,
            NoSpecificIngredientInFullDayOfEatingError,
        )

        # Save for later to calculate average daily cost of mealplan.
        specificingredient_dict_list_mealplan.append(
            specificingredient_dict_list
            )

        result_total_nutrition_fulldayofeating,\
            result_total_nutrition_fulldayofeating_rounded =\
            calculate_total_nutrition_fulldayofeating(
                specificingredient_dict_list,
                ALL_NUTRIENTS_AND_DEFAULT_UNITS,
                set_to_zero_if_none,
            )

        result_total_nutrition_fulldayofeating_list.append(
            result_total_nutrition_fulldayofeating
            )

    # Initialize the dictionary which will store the results
    result_average_nutrition_mealplan = {}
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        nutrient_name = dict_k['name']
        new_dict = {nutrient_name: 0}
        result_average_nutrition_mealplan.update(
            new_dict
        )

    # Iterate through all the nutrients. For each nutrient, calculate the
    # average over the full days of eating contained in the mealplan.
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        nutrient_name = dict_k['name']

        # Sum that nutrient up over all the full days of eating in the mealplan.
        nutrient_sum_mealplan = 0

        for result_total_nutrition_fulldayofeating in \
                result_total_nutrition_fulldayofeating_list:
            nutrient_sum_mealplan = \
                nutrient_sum_mealplan + \
                result_total_nutrition_fulldayofeating[nutrient_name]

        number_of_fulldayofeating_in_mealplan = \
            len(result_total_nutrition_fulldayofeating_list)
        nutrient_average_in_mealplan = \
            nutrient_sum_mealplan / number_of_fulldayofeating_in_mealplan

        nutrient_average_in_mealplan_rounded = \
            round(nutrient_average_in_mealplan, 0)

        result_average_nutrition_mealplan[nutrient_name] =\
            nutrient_average_in_mealplan_rounded

    # Make the result_average_nutrition_mealplan into a list.
    result_average_nutrition_mealplan_values = []
    nutrient_name_list = []
    for key, value in result_average_nutrition_mealplan.items():
        result_average_nutrition_mealplan_values.append(value)
        nutrient_name_list.append(key)

    # Make the default units into a list and display them in the table.
    default_unit_list = []
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        default_unit_list.append(dict_k['default_unit'])

    # =========================================================================
    # Calculate % Target

    nutrientprofile_dict = query_nutrientprofile_of_mealplan(
        id_mealplan,
        Mealplan,
        NutrientProfile,
    )

    result_percentage_of_target_amount_str,\
        result_percentage_of_target_amount_numbers = \
        calculate_percentage_of_target_amount(
            nutrientprofile_dict,
            result_average_nutrition_mealplan,
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

    # =========================================================================

    # 'Max amount' and 'tolerable upper intake' are used interchangeably.
    result_total_nutrition_fulldayofeating = copy.deepcopy(
        result_average_nutrition_mealplan
    )
    result_percent_max_dict, \
    result_percentage_of_tolerable_upper_intake_str_list, \
    result_percentage_of_tolerable_upper_intake_numbers_list = \
        calculate_percent_max_fulldayofeating(
            nutrientprofile_dict,
            result_total_nutrition_fulldayofeating,
        )

    # =========================================================================

    # TODO Based on the ratios between the sum of the total nutrition for a
    #   given nutrient to that nutrient's target value and tolerable upper
    #  intake,
    #  judge the total nutrition as either the right amount, too little or too
    #  much.

    result_judge_total_nutrition, \
    result_judge_total_nutrition_css_class_name = judge_total_nutrition(
        result_percentage_of_target_amount_numbers_list,
        result_percentage_of_tolerable_upper_intake_numbers_list,
        set_to_zero_if_none,
    )

    aggregated_total_nutrition_fulldayofeating = \
        zip(
            nutrient_name_list,
            result_average_nutrition_mealplan_values,
            default_unit_list,
            result_percentage_of_target_amount_list,
            result_percentage_of_tolerable_upper_intake_str_list,
            result_judge_total_nutrition,
            result_judge_total_nutrition_css_class_name,
            )

    # Get the name of the mealplan
    queryset_mealplan_name = \
        Mealplan.objects.filter(id=id_mealplan).values('name')
    mealplan_name = list(queryset_mealplan_name)[0]['name']
    # print('mealplan_name')
    # pprint.pprint(mealplan_name)

    # Calculate the average daily cost of a mealplan.

    # Calculate the total price for each FullDayOfEating.
    # Collect the price for each day in a list.
    fulldayofeating_price_collection_list = []
    for specificingredient_dict_list in specificingredient_dict_list_mealplan:
        total_price_fulldayofeating_result_dict = \
            calculate_total_price_fulldayofeating(
                specificingredient_dict_list,
            )
        fulldayofeating_price_collection_list.append(
            total_price_fulldayofeating_result_dict
        )

    mealplan_total_price_dict = {
        'price_sum_mealplan': 0,
        'average_price_mealplan': 0,
        'average_price_mealplan_rounded': 0,
        'total_price_currency': 'currency',
        'total_price_rounded': 0,
        }
    # Sum up the prices of the FullDayOfEating to get the total price of the
    # Mealplan.
    for price_dict in fulldayofeating_price_collection_list:
        mealplan_total_price_dict['price_sum_mealplan'] = \
            mealplan_total_price_dict['price_sum_mealplan'] + \
            price_dict['total_price']

    # From the sum, calculate the average price
    n_fulldayofeating_objects_in_mealplan = \
        len(fulldayofeating_price_collection_list)

    mealplan_total_price_dict['average_price_mealplan'] = \
        mealplan_total_price_dict['price_sum_mealplan']\
        / n_fulldayofeating_objects_in_mealplan

    mealplan_total_price_dict['average_price_mealplan_rounded'] = \
        round(mealplan_total_price_dict['average_price_mealplan'], 2)

    # It is assumed that all mealplans have the same currency. The currency
    # of the first full day of eating is selected.
    mealplan_total_price_dict['total_price_currency'] = \
        fulldayofeating_price_collection_list[0]['total_price_currency']

    # Write code above this line

    context = {
        'aggregated_total_nutrition_fulldayofeating':
        aggregated_total_nutrition_fulldayofeating,
        'mealplan_name':
        mealplan_name,
        'mealplan_total_price_dict':
        mealplan_total_price_dict,
        'id_mealplan':
        id_mealplan,
    }
    return render(
        request,
        'measuredfood/mealplan_averagenutrition.html',
        context
        )


def copy_mealplan_to_user(request, id_mealplan):
    """
    From the public available mealplans, copy a mealplan to the user's
    collection of mealplans.
    :return:
    """

    # Do the copying the manual and long way.

    # Find all the FullDayOfEating objects associated with the Mealplan.

    # Copy each FullDayOfEating object as you did before.

    # Find the NutrientProfile associated with the Mealplan as a whole.

    # Copy all the FullDayOfEating objects associated with the Mealplan.
    original_mealplan = Mealplan.objects.get(
        id=id_mealplan
    )

    mealplan_copy = copy.deepcopy(original_mealplan)
    mealplan_copy.author = request.user
    mealplan_copy.save()

    mealplan_list = Mealplan.objects.filter(
        author=request.user
    ).order_by('name')

    print('mealplan_list')
    print(mealplan_list)

    context = {'mealplan_list': mealplan_list}

    return render(
        request,
        'measuredfood/fulldayofeating_list.html',
        context
    )
