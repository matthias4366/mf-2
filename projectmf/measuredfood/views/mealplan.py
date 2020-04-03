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

from measuredfood.utils.set_to_zero_if_none\
    import set_to_zero_if_none

from measuredfood.utils.query.query_nutrientprofile_of_fulldayofeating\
    import query_nutrientprofile_of_fulldayofeating

from measuredfood.utils.calculate_average_of_specificingredient_group import \
    calculate_average_of_specificingredient_group

from measuredfood.utils.undo_calculate_average_of_specificingredient_group \
    import undo_calculate_average_of_specificingredient_group

from measuredfood.utils.fulldayofeating\
    .query_input_and_calculate_fulldayofeating\
    import query_input_and_calculate_fulldayofeating

from measuredfood.utils.query.query_specificnutrienttarget_of_fulldayofeating \
    import query_specificnutrienttarget_of_fulldayofeating

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

from pathlib import Path

path_to_nutrient_dict_list_json = Path(
    __file__).parent.parent.joinpath('data').joinpath('nutrient_dict_list.json')

with open(path_to_nutrient_dict_list_json, 'r') as fp:
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


def copy_mealplan_to_user(request, id_mealplan):
    """
    From the public available mealplans, copy a mealplan to the user's
    collection of mealplans.
    :return:
    """

    # TODO: Finish this function. It is complicated and not absolutely
    #  necessary so it can be skipped for now.

    # # Do the copying of the mealplan the manual and long way.
    #
    # # Find all the FullDayOfEating objects associated with the Mealplan.
    # specificfulldayofeating_of_mealplan_orig = \
    #     SpecificFullDayOfEating.objects.filter(
    #         mealplan=id_mealplan
    #     )
    #
    # list_unique_nutrient_profile_id = []
    # # Copy each SpecificFullDayOfEating object.
    # for specific_full_day_of_eating in specificfulldayofeating_of_mealplan_orig:
    #     id_fulldayofeating = specific_full_day_of_eating.fulldayofeating
    #
    #     # Copy the nutrient profile:
    #     nutrient_profile_id = FullDayOfEating.objects.get(
    #         id=id_fulldayofeating
    #     ).nutrient_profile.id
    #     if nutrient_profile_id not in list_unique_nutrient_profile_id:
    #         list_unique_nutrient_profile_id.append(
    #             nutrient_profile_id
    #         )
    #
    # # Avoid copying the same nutrient profile multiple twice just because it
    # # is associated with multiple FullDayOfEating objects in the Mealplan.
    # for unique_id_nutrient_profile in list_unique_nutrient_profile_id:
    #     nutrient_profile_copy = NutrientProfile.objects.get(
    #         id=unique_id_nutrient_profile
    #     )
    #     nutrient_profile_copy.pk = None
    #     nutrient_profile_copy.author = request.user
    #     nutrient_profile_copy.save()

    # Copy each FullDayOfEating object as you did before.

    mealplan_list = Mealplan.objects.filter(
        author=request.user
    ).order_by('name')

    context = {'mealplan_list': mealplan_list}

    return render(
        request,
        'measuredfood/mealplan_list.html',
        context
    )
