from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import copy
from measuredfood.forms import (
    FullDayOfEatingForm,
    SpecificIngredientFormset,
    SpecificNutrientTargetFormset
    )
from measuredfood.models import (
    RawIngredient2,
    NutrientProfile,
    NutrientTargetSelection,
    TolerableUpperIntake,
    SpecificNutrientTarget,
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
from measuredfood.utils.calculate_fulldayofeating\
import calculate_fulldayofeating
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

from measuredfood.utils.query.query_ingredients_fulldayofeating\
import query_ingredients_fulldayofeating

from measuredfood.utils.calculate_total_price_fulldayofeating\
import calculate_total_price_fulldayofeating

from measuredfood.utils.query.query_nutrientprofile_of_fulldayofeating\
import query_nutrientprofile_of_fulldayofeating

from measuredfood.utils.query.query_tolerableupperintake_of_fulldayofeating\
import query_tolerableupperintake_of_fulldayofeating

from measuredfood.utils.undo_calculate_average_of_specificingredient_group\
import undo_calculate_average_of_specificingredient_group

from measuredfood.utils.calculate_average_of_specificingredient_group \
import calculate_average_of_specificingredient_group

from measuredfood.utils.fulldayofeating.query_input_and_calculate_fulldayofeating\
import query_input_and_calculate_fulldayofeating

from measuredfood.utils.query.query_result_calculation_fulldayofeating \
import query_result_calculation_fulldayofeating

from measuredfood.utils.query.query_specificnutrienttarget_of_fulldayofeating\
import query_specificnutrienttarget_of_fulldayofeating

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

        formset_specificingredient = SpecificIngredientFormset(
            request.POST,
            instance=fulldayofeating_object
            )
        # I do not know if this part is necessary. It seems to work without.
        # Allow the user to only add RawIngredient2s from their own collection.
        for form in formset_specificingredient:
            form.fields['rawingredient'].queryset = \
            RawIngredient2.objects.filter(
                author = request.user.id
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
        # Allow the user to only add NutrientProfiles from their own collection.
        form_fulldayofeating.fields['nutrient_profile'].queryset = \
        NutrientProfile.objects.filter(
            author = request.user.id
            )

        formset_specificingredient = SpecificIngredientFormset(
            instance=fulldayofeating_object
            )

        # Allow the user to only add RawIngredient2s from their own collection.
        for form in formset_specificingredient:
            form.fields['rawingredient'].queryset = \
            RawIngredient2.objects.filter(
                author = request.user.id
                )

        formset_specificnutrienttarget = SpecificNutrientTargetFormset(
            instance=fulldayofeating_object,
        )

        context = {
            'formset_specificingredient': formset_specificingredient,
            'form_fulldayofeating': form_fulldayofeating,
            'id_fulldayofeating': id_fulldayofeating,
            'formset_specificnutrienttarget': formset_specificnutrienttarget,
            }
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

    result_calculate_fulldayofeating,\
    specificingredient_dict_list = \
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
        RawIngredient2,
        pprint,
        FullDayOfEating,
        NutrientProfile,
        SpecificNutrientTarget,
        copy,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        np,
    )

    result_calculation_fulldayofeating = \
    query_result_calculation_fulldayofeating(
        id_fulldayofeating,
        SpecificIngredient,
        RawIngredient2,
        )

    # Calculate the total nutrition of the full day of eating
    result_total_nutrition_fulldayofeating,\
    result_total_nutrition_fulldayofeating_rounded =\
    calculate_total_nutrition_fulldayofeating(
        specificingredient_dict_list,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        pprint,
        copy,
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
        pprint,
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

    # print('\n result_percentage_of_target_amount_numbers_list \n')
    # pprint.pprint(result_percentage_of_target_amount_numbers_list)

    # Calculate the percentage of the tolerable upper limit.
    tolerableupperintake_dict = query_tolerableupperintake_of_fulldayofeating(
        id_fulldayofeating,
        FullDayOfEating,
        TolerableUpperIntake,
    )
    result_percentage_of_tolerable_upper_intake_str,\
    result_percentage_of_tolerable_upper_intake_numbers = \
    calculate_percentage_of_tolerable_upper_intake(
        tolerableupperintake_dict,
        result_total_nutrition_fulldayofeating,
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

    # Make the default units into a list and display them in the table.
    default_unit_list = []
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        default_unit_list.append(dict_k['default_unit'])

    # Based on the ratios between the sum of the total nutrition for a
    # given nutrient to that nutrient's target value and tolerable upper intake,
    # judge the total nutrition as either the right amount, too little or too
    # much.
    result_judge_total_nutrition,\
    result_judge_total_nutrition_css_class_name = judge_total_nutrition(
        result_percentage_of_target_amount_numbers_list,
        result_percentage_of_tolerable_upper_intake_numbers_list,
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
    # print('\n aggregated_total_nutrition_fulldayofeating \n')
    # pprint.pprint(aggregated_total_nutrition_fulldayofeating)


    total_price_fulldayofeating_result_dict = calculate_total_price_fulldayofeating(
        specificingredient_dict_list,
        pprint,
    )

    context = {'id_fulldayofeating': id_fulldayofeating,
               'result_calculation_fulldayofeating': \
               result_calculation_fulldayofeating,
               'result_calculate_fulldayofeating':\
               result_calculate_fulldayofeating,
               'aggregated_total_nutrition_fulldayofeating': \
               aggregated_total_nutrition_fulldayofeating,
               'result_percentage_of_target_amount':\
               result_percentage_of_target_amount_str,
               'total_price_fulldayofeating_result_dict':\
               total_price_fulldayofeating_result_dict,
               'negative_result':\
               result_calculate_fulldayofeating['errors']['negative_result'],
               'mismatch':\
               result_calculate_fulldayofeating['errors']['mismatch']
               }

    # TODO: use reverse function instead
    return render(
        request,
        'measuredfood/fulldayofeating_calculation_result.html',
        context
        )
