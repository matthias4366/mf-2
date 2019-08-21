from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import copy
from measuredfood.forms import (
    FullDayOfEatingForm,
    SpecificIngredientFormset
    )
from measuredfood.models import (
    RawIngredient2,
    NutrientProfile,
    NutrientTargetSelection,
    TolerableUpperIntake,
)
from measuredfood.models import FullDayOfEating, SpecificIngredient
from django.urls import reverse, reverse_lazy
# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from measuredfood.utils import fulldayofeating_calculate
import pprint
from django.contrib.auth.decorators import login_required
import pprint
from measuredfood.ingredient_properties2 import (
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
from measuredfood.utils.calculate_percentage_of_tolerable_upper_intake\
import calculate_percentage_of_tolerable_upper_intake
from measuredfood.utils.judge_total_nutrition\
import judge_total_nutrition
from measuredfood.utils.query_ingredients_fulldayofeating\
import query_ingredients_fulldayofeating
from measuredfood.utils.calculate_total_price_fulldayofeating\
import calculate_total_price_fulldayofeating

@login_required
def create_fulldayofeating_view(request):
    """
    Largely copied from the update_fulldayofeating function. Always edit that
    function first and copy the changes to the create_fulldayofeating function.
    """

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(request.user.id, request.POST)
        if form_fulldayofeating.is_valid():
            form_fulldayofeating.instance.author = request.user
            form_fulldayofeating.save()
            return redirect('list-fulldayofeating')
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
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        FullDayOfEating,
        id_fulldayofeating
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)
    # The user is the author, proceed.

    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(
            request.user.id,
            request.POST,
            instance=fulldayofeating_object
            )
        # I do not know if this part is necessary. It seems to work without.
        # Allow the user to only add NutrientProfiles from their own collection.
        form_fulldayofeating.fields['nutrient_profile'].queryset = \
        NutrientProfile.objects.filter(
            author = request.user.id
            )
        # Allow the user to only add NutrientTargetSelections from their own
        # collection.
        form_fulldayofeating.fields['nutrient_target_selection'].queryset = \
        NutrientTargetSelection.objects.filter(
            author = request.user.id
            )

        formset = SpecificIngredientFormset(
            request.POST,
            instance=fulldayofeating_object
            )
        # I do not know if this part is necessary. It seems to work without.
        # Allow the user to only add RawIngredient2s from their own collection.
        for form in formset:
            form.fields['rawingredient'].queryset = \
            RawIngredient2.objects.filter(
                author = request.user.id
                )

        if formset.is_valid() and form_fulldayofeating.is_valid():
            formset.save()
            form_fulldayofeating.save()
            return redirect(
                'update-fulldayofeating',
                id_fulldayofeating=fulldayofeating_object.id
                )
    else:
        form_fulldayofeating = FullDayOfEatingForm(
            request.user.id,
            instance=fulldayofeating_object
            )
        # Allow the user to only add NutrientProfiles from their own collection.
        form_fulldayofeating.fields['nutrient_profile'].queryset = \
        NutrientProfile.objects.filter(
            author = request.user.id
            )

        formset = SpecificIngredientFormset(instance=fulldayofeating_object)
        # Allow the user to only add RawIngredient2s from their own collection.
        for form in formset:
            form.fields['rawingredient'].queryset = \
            RawIngredient2.objects.filter(
                author = request.user.id
                )
            # Allow the user to only add NutrientTargetSelections from their own
            # collection.
            form_fulldayofeating.fields['nutrient_target_selection'].queryset = \
            NutrientTargetSelection.objects.filter(
                author = request.user.id
                )

        context = {'formset': formset,
                   'form_fulldayofeating': form_fulldayofeating,
                   'id_fulldayofeating': id_fulldayofeating}
        # TODO: use reverse function instead
        return render(request,'measuredfood/fulldayofeating_form.html', context)


class ListFullDayOfEating(
    LoginRequiredMixin,
    ListView
):
    model = FullDayOfEating
    def get_queryset(self):
        return FullDayOfEating.objects.filter(
            author = self.request.user
        ).order_by('name')


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
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        FullDayOfEating,
        id_fulldayofeating
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)
    # The user is the author, proceed.

    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)

    specificingredient_id_and_calculated_amount = \
    fulldayofeating_calculate.calculate_fulldayofeating(
        id_fulldayofeating,
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
    # print('\n specificingredient_id_and_calculated_amount \n')
    # pprint.pprint(specificingredient_id_and_calculated_amount)

    # Save the results to the database:
    save_fulldayofeating_calculation_result_to_database(
        specificingredient_id_and_calculated_amount,
        SpecificIngredient
    )

    result_calculation_fulldayofeating = \
    query_result_calculation_fulldayofeating(id_fulldayofeating)

    # Calculate the total nutrition of the full day of eating
    result_total_nutrition_fulldayofeating,\
    result_total_nutrition_fulldayofeating_rounded =\
    calculate_total_nutrition_fulldayofeating(
        id_fulldayofeating,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        pprint,
        copy,
        SpecificIngredient,
        RawIngredient2,
        set_to_zero_if_none,
    )

    # Make the result_total_nutrition_fulldayofeating_rounded into a list.
    result_total_nutrition_fulldayofeating_rounded_list = []
    nutrient_name_list = []
    for key, value in result_total_nutrition_fulldayofeating_rounded.items():
        result_total_nutrition_fulldayofeating_rounded_list.append(value)
        nutrient_name_list.append(key)

    # print('\n result_total_nutrition_fulldayofeating_rounded \n')
    # pprint.pprint(result_total_nutrition_fulldayofeating_rounded)

    # Calculate the ratio of the total nutrition in the full day of eating
    # in relation to the target amounts in the nutrient profile and
    # express the result as a percentage.

    result_percentage_of_target_amount_str,\
    result_percentage_of_target_amount_numbers = \
    calculate_percentage_of_target_amount(
        result_total_nutrition_fulldayofeating,
        pprint,
        id_fulldayofeating,
        FullDayOfEating,
        NutrientProfile,
        set_to_zero_if_none,
    )

    # print('\n result_percentage_of_target_amount_str \n')
    # pprint.pprint(result_percentage_of_target_amount_str)

    # Make the result_percentage_of_target_amount_str into a list
    result_percentage_of_target_amount_list = []
    for key, value in result_percentage_of_target_amount_str.items():
        result_percentage_of_target_amount_list.append(value)

    # Make the result_percentage_of_target_amount_numbers into a list
    result_percentage_of_target_amount_numbers_list = []
    for key, value in result_percentage_of_target_amount_numbers.items():
        result_percentage_of_target_amount_numbers_list.append(value)

    # Calculate the percentage of the tolerable upper limit.
    result_percentage_of_tolerable_upper_intake_str,\
    result_percentage_of_tolerable_upper_intake_numbers = \
    calculate_percentage_of_tolerable_upper_intake(
        result_total_nutrition_fulldayofeating,
        id_fulldayofeating,
        pprint,
        FullDayOfEating,
        TolerableUpperIntake,
        set_to_zero_if_none,
    )

    # print('\n result_percentage_of_tolerable_upper_intake_str \n')
    # pprint.pprint(result_percentage_of_tolerable_upper_intake_str)

    # Make the result_percentage_of_target_amount_str into a list
    result_percentage_of_tolerable_upper_intake_str_list = []
    for key, value in result_percentage_of_tolerable_upper_intake_str.items():
        result_percentage_of_tolerable_upper_intake_str_list.append(value)

    # Make the result_percentage_of_target_amount_numbers into a list
    result_percentage_of_tolerable_upper_intake_numbers_list = []
    for key, value in result_percentage_of_tolerable_upper_intake_numbers.items():
        result_percentage_of_tolerable_upper_intake_numbers_list.append(value)

    # Make the default units into a list and display them in the table.
    default_unit_list = []
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        default_unit_list.append(dict_k['default_unit'])

    # Based on the ratios between the sum of the total nutrition for a
    # given nutrient to that nutrient's target value and tolerable upper intake,
    # judge the total nutrition as either the right amount, too little or too
    # much.
    result_judge_total_nutrition = judge_total_nutrition(
        result_percentage_of_target_amount_numbers_list,
        result_percentage_of_tolerable_upper_intake_numbers_list,
    )
    # print('\n result_judge_total_nutrition \n')
    # pprint.pprint(result_judge_total_nutrition)

    aggregated_total_nutrition_fulldayofeating = \
    zip(
        nutrient_name_list,
        result_total_nutrition_fulldayofeating_rounded_list,
        default_unit_list,
        result_percentage_of_target_amount_list,
        result_percentage_of_tolerable_upper_intake_str_list,
        result_judge_total_nutrition,
        )
    # print('\n aggregated_total_nutrition_fulldayofeating \n')
    # pprint.pprint(aggregated_total_nutrition_fulldayofeating)

    # Calculate the total price
    # Query the SpecificIngredient objects related to the FullDayOfEating.
    # TODO: There might be mulitple queries doing the same thing,
    # i.e. getting SpecificIngredient objects related to the FullDayOfEating

    specificingredient_dict_list = query_ingredients_fulldayofeating(
        id_fulldayofeating,
        SpecificIngredient,
        RawIngredient2,
        pprint,
    )

    total_price_fulldayofeating_result_dict = calculate_total_price_fulldayofeating(
        specificingredient_dict_list,
        pprint,
    )


    context = {'id_fulldayofeating': id_fulldayofeating,
               'result_calculation_fulldayofeating': \
               result_calculation_fulldayofeating,
               'aggregated_total_nutrition_fulldayofeating': \
               aggregated_total_nutrition_fulldayofeating,
               'result_percentage_of_target_amount':\
               result_percentage_of_target_amount_str,
               'total_price_fulldayofeating_result_dict':\
               total_price_fulldayofeating_result_dict
               # TODO: the error_message_calculate_fulldayofeating needs to
               # be given to the template and rendered in the html.
               }

    # TODO: use reverse function instead
    return render(
        request,
        'measuredfood/fulldayofeating_calculation_result.html',
        context
        )

def query_result_calculation_fulldayofeating(id_fulldayofeating):
    """
    In the page fulldayofeating_calculate.html, at the bottom, a table
    should display the results of the calculation. Here, the results are
    queried and given to the context dictionary.
    """
    # Get the names of the raw ingredients belonging to the fulldayofeating
    queryset_specificingredient = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    list_specificingredient_id = [
        s.id for s in queryset_specificingredient
        ]

    # Get the information about the specific ingredients belonging to the
    # fulldayofeating
    list_of_dict_specificingredient = list(
        queryset_specificingredient.values()
        )

    result_calculation_fulldayofeating = []
    for k in range(len(list_of_dict_specificingredient)):
        specific_ingredient_obj = SpecificIngredient.objects.get(
                    id=list_specificingredient_id[k]
                    )

        calculated_amount_k = getattr(specific_ingredient_obj, 'calculated_amount')
        base_amount_unit_k = getattr(specific_ingredient_obj, 'base_amount_unit')

        specific_ingredient_k_id = specific_ingredient_obj.id

        rawingredient_k_id = SpecificIngredient.objects.filter(
                    id=list_specificingredient_id[k]
                    ).values('rawingredient_id')
        rawingredient_k_id = list(rawingredient_k_id)
        rawingredient_k_id = rawingredient_k_id[0]
        rawingredient_k_id = rawingredient_k_id['rawingredient_id']

        rawingredient_k_queryset = RawIngredient2.objects.filter(
            id = rawingredient_k_id
        )
        name_k = rawingredient_k_queryset.values('name')
        name_k = list(name_k)[0]['name']

        buy_here_link_k = rawingredient_k_queryset.values('buy_here_link')
        buy_here_link_k = list(buy_here_link_k)[0]['buy_here_link']

        merged_dict_k = {
            'specificingredient_id': list_specificingredient_id[k],
            'calculated_amount': calculated_amount_k,
             'base_amount_unit': base_amount_unit_k,
             'name': name_k,
             'buy_here_link': buy_here_link_k
        }
        result_calculation_fulldayofeating.append(merged_dict_k)

    return result_calculation_fulldayofeating
