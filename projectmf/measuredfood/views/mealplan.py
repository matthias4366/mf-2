from django.shortcuts import render
from django.http import HttpResponse
import copy

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from measuredfood.forms import UserRegisterForm

# imports for the view to create raw ingredients
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)
from measuredfood.models import (
    Mealplan,
    FullDayOfEating,
    SpecificFullDayOfEating,
    SpecificIngredient,
    NutrientProfile,
    RawIngredient2,
    NutrientTargetSelection,
    TolerableUpperIntake,
)
from measuredfood.forms import (
    MealplanForm,
    SpecificFullDayOfEatingFormset
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from measuredfood.utils.check_if_author import check_if_author
import pprint
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
import numpy as np
from measuredfood.utils import fulldayofeating_calculate
from measuredfood.utils.save_fulldayofeating_calculation_result_to_database \
import save_fulldayofeating_calculation_result_to_database
from measuredfood.utils.query_ingredients_fulldayofeating\
import query_ingredients_fulldayofeating
from measuredfood.utils.calculate_total_nutrition_fulldayofeating \
import calculate_total_nutrition_fulldayofeating
from measuredfood.utils.set_to_zero_if_none\
import set_to_zero_if_none
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
)
from measuredfood.utils.query_nutrientprofile_of_fulldayofeating\
import query_nutrientprofile_of_fulldayofeating
from measuredfood.utils.calculate_percentage_of_target_amount\
import calculate_percentage_of_target_amount
from measuredfood.utils.query_nutrientprofile_of_mealplan\
import query_nutrientprofile_of_mealplan

from measuredfood.utils.query.query_tolerableupperintake_of_mealplan import\
query_tolerableupperintake_of_mealplan

from measuredfood.utils.calculate_percentage_of_tolerable_upper_intake import\
calculate_percentage_of_tolerable_upper_intake

from measuredfood.utils.judge_total_nutrition import\
judge_total_nutrition

@login_required
def create_mealplan_view(request):
    view_type = 'create'

    if request.method == 'POST':
        form_mealplan = MealplanForm(request.POST)
        if form_mealplan.is_valid():
            form_mealplan.instance.author = request.user
            form_mealplan.save()
            return redirect('list-mealplan')
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
    view_type = 'update'

    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        Mealplan,
        id_mealplan
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)
    # The user is the author, proceed.

    mealplan_object = Mealplan.objects.get(pk = id_mealplan)

    if request.method == 'POST':
        form_mealplan = MealplanForm(
            request.POST,
            instance = mealplan_object
        )
        formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
            request.POST,
            instance = mealplan_object
        )

        if form_mealplan.is_valid() and \
        formset_specificfulldayofeating.is_valid():
            formset_specificfulldayofeating.save()
            form_mealplan.save()
            return redirect(
                'update-mealplan',
                id_mealplan = mealplan_object.id
                )
    else:
        form_mealplan = MealplanForm(instance = mealplan_object)
        formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
            instance = mealplan_object
        )
        # Only let the user select FullDayOfEating objects from their own
        # collection.
        for form in formset_specificfulldayofeating:
            form.fields['fulldayofeating'].queryset = \
            FullDayOfEating.objects.filter(
                author = request.user.id
            )

        context = {
            'form_mealplan': form_mealplan,
            'formset_specificfulldayofeating': formset_specificfulldayofeating,
            'id_mealplan': mealplan_object.id,
            'view_type': view_type
        }
        # TODO: use reverse_lazy instead of hard coding the name of the html file.
        return render(request, 'measuredfood/mealplan_form.html', context)

@login_required
def shoppinglist_view(request, id_mealplan):

    # From id_mealplan, get all the related SpecificFullDayOfEating objects.
    queryset_specificfulldayofeating = SpecificFullDayOfEating.objects.filter(
        mealplan = id_mealplan
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
        # TODO: A for loop is used for a dictionary that only has one entry.
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
        id_fulldayofeating_to_recalculate = id_list_no_duplications[k]

        specificingredient_id_and_calculated_amount = \
        fulldayofeating_calculate.calculate_fulldayofeating(
            id_fulldayofeating_to_recalculate,
            SpecificIngredient,
            FullDayOfEating,
            NutrientProfile,
            NutrientTargetSelection,
            RawIngredient2,
            pprint,
            copy,
            ALL_NUTRIENTS_AND_DEFAULT_UNITS,
            np
            )
        # Save the results to the database:
        save_fulldayofeating_calculation_result_to_database(
            specificingredient_id_and_calculated_amount,
            SpecificIngredient
        )

    # Sum up the calculated amounts.
    # Initiate a dictionary shopping_list_dict which will have the format
    # {'RawIngredient_name': sum total amount}.
    shopping_list_dict = {}

    # Iterate over the id_list_with_duplications.
    for id_fulldayofeating_k in id_list_with_duplications:
        queryset_specificingredient_for_sum = SpecificIngredient.objects.filter(
            fulldayofeating = id_fulldayofeating_k
        ).values()
        list_specificingredient_for_sum = list(queryset_specificingredient_for_sum)
        # print('\n\n list_specificingredient_for_sum')
        # pprint.pprint(list_specificingredient_for_sum)

        # For each FullDayOfEating in
        # that list, iterate over all the SpecificIngredients.
        for dict_specificingredient_k in list_specificingredient_for_sum:
            # For each SpecificIngredient, get the name of the associated RawIngredient2.
            rawingredient_id = dict_specificingredient_k['rawingredient_id']
            query_rawingredient_name = RawIngredient2.objects.filter(
                id = rawingredient_id
            ).values('name')
            # print('\n\n query_rawingredient_name')
            # pprint.pprint(query_rawingredient_name)

            rawingredient_name = list(query_rawingredient_name)[0]['name']
            # print('\n\n rawingredient_name')
            # pprint.pprint(rawingredient_name)

            # Check if the name of the RawIngredient2 is already in the
            # shopping_list_dict. If it is not, add it and initialize the sum total
            # amount as 0.
            if rawingredient_name not in shopping_list_dict:
                new_dict = {rawingredient_name: 0}
                shopping_list_dict.update(new_dict)

            # After that, add the calculated_amount of the SpecificIngredient which
            # is related to the RawIngredient2 to the sum total amount.
            shopping_list_dict[rawingredient_name] = \
            shopping_list_dict[rawingredient_name] \
            + dict_specificingredient_k['calculated_amount']


    # print('\n\n shopping_list_dict')
    # pprint.pprint(shopping_list_dict)
    context = {
        'results_shopping_list': shopping_list_dict,
        'id_mealplan': id_mealplan,
        }
    # print('\n\n context')
    # pprint.pprint(context)
    return render(request, 'measuredfood/shoppinglist.html', context)


class ListMealplan(
    LoginRequiredMixin,
    ListView
):
    model = Mealplan
    def get_queryset(self):
        return Mealplan.objects.filter(
            author = self.request.user
        ).order_by('name')


class DetailMealplan(UserPassesTestMixin, DetailView):
    model = Mealplan

    def test_func(self):
        mealplan = self.get_object()
        if self.request.user == mealplan.author:
            return True
        return False


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
        mealplan = id_mealplan
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
        # TODO: A for loop is used for a dictionary that only has one entry.
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
        id_fulldayofeating_to_recalculate = id_list_no_duplications[k]

        specificingredient_id_and_calculated_amount = \
        fulldayofeating_calculate.calculate_fulldayofeating(
            id_fulldayofeating_to_recalculate,
            SpecificIngredient,
            FullDayOfEating,
            NutrientProfile,
            NutrientTargetSelection,
            RawIngredient2,
            pprint,
            copy,
            ALL_NUTRIENTS_AND_DEFAULT_UNITS,
            np
            )
        # Save the results to the database:
        save_fulldayofeating_calculation_result_to_database(
            specificingredient_id_and_calculated_amount,
            SpecificIngredient
        )

    # The calculated_amount values for the FullDayOfEating objects have been
    # recalculated. Now to the calculation of the average daily nutrition.

    # Make a list which contains the average nutrition for each full day of
    # eating in the mealplan. This list will later be used to calculate the
    # average.
    result_total_nutrition_fulldayofeating_list = []

    # Calculate the nutrition sum for each FullDayOfEating.
    # Iterate over the id_list_with_duplications.
    for id_fulldayofeating in id_list_with_duplications:

        specificingredient_dict_list = query_ingredients_fulldayofeating(
            id_fulldayofeating,
            SpecificIngredient,
            RawIngredient2,
            pprint,
        )

        result_total_nutrition_fulldayofeating,\
        result_total_nutrition_fulldayofeating_rounded =\
        calculate_total_nutrition_fulldayofeating(
            specificingredient_dict_list,
            ALL_NUTRIENTS_AND_DEFAULT_UNITS,
            pprint,
            copy,
            set_to_zero_if_none,
        )

        print('\n result_total_nutrition_fulldayofeating \n')
        pprint.pprint(result_total_nutrition_fulldayofeating)

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
        pprint,
        set_to_zero_if_none,
    )

    # Make the result_percentage_of_target_amount_str into a list
    result_percentage_of_target_amount_list = []
    for key, value in result_percentage_of_target_amount_str.items():
        result_percentage_of_target_amount_list.append(value)

    # =========================================================================

    # Calculate the percentage of the tolerable upper limit.
    tolerableupperintake_dict = query_tolerableupperintake_of_mealplan(
        id_mealplan,
        Mealplan,
        TolerableUpperIntake,
        pprint,
    )
    result_percentage_of_tolerable_upper_intake_str,\
    result_percentage_of_tolerable_upper_intake_numbers = \
    calculate_percentage_of_tolerable_upper_intake(
        tolerableupperintake_dict,
        result_average_nutrition_mealplan,
        pprint,
        set_to_zero_if_none,
    )

    # Make the result_percentage_of_tolerable_upper_intake_str into a list
    result_percentage_of_tolerable_upper_intake_str_list = []
    for key, value in result_percentage_of_tolerable_upper_intake_str.items():
        result_percentage_of_tolerable_upper_intake_str_list.append(value)

    # Make the result_percentage_of_tolerable_upper_intake_numbers into a list
    result_percentage_of_tolerable_upper_intake_numbers_list = []
    for key, value in result_percentage_of_tolerable_upper_intake_numbers.items():
        result_percentage_of_tolerable_upper_intake_numbers_list.append(value)

    # =========================================================================

    # Based on the ratios between the sum of the total nutrition for a
    # given nutrient to that nutrient's target value and tolerable upper intake,
    # judge the total nutrition as either the right amount, too little or too
    # much.
    # Make the result_percentage_of_target_amount_numbers into a list
    result_percentage_of_target_amount_numbers_list = []
    for key, value in result_percentage_of_target_amount_numbers.items():
        result_percentage_of_target_amount_numbers_list.append(value)
    result_judge_total_nutrition,\
    result_judge_total_nutrition_css_class_name = judge_total_nutrition(
        result_percentage_of_target_amount_numbers_list,
        result_percentage_of_tolerable_upper_intake_numbers_list,
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

    # Write code above this line

    context = {
        'aggregated_total_nutrition_fulldayofeating':\
        aggregated_total_nutrition_fulldayofeating
    }
    return render(
        request,
        'measuredfood/mealplan_averagenutrition.html',
        context
        )
