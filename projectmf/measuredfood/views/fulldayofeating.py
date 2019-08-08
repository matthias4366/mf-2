from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import copy
from measuredfood.forms import (
    FullDayOfEatingForm,
    SpecificIngredientFormset
    )
from measuredfood.models import (
    RawIngredient,
    NutrientProfile
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
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_NUTRITION
)
import numpy as np
from measuredfood.utils.check_if_author import check_if_author

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

        formset = SpecificIngredientFormset(
            request.POST,
            instance=fulldayofeating_object
            )
        # I do not know if this part is necessary. It seems to work without.
        # Allow the user to only add RawIngredients from their own collection.
        for form in formset:
            form.fields['rawingredient'].queryset = \
            RawIngredient.objects.filter(
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
        # Allow the user to only add RawIngredients from their own collection.
        for form in formset:
            form.fields['rawingredient'].queryset = \
            RawIngredient.objects.filter(
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
        RawIngredient,
        pprint,
        copy,
        INGREDIENT_FIELDS_NUTRITION,
        np
        )
    # print('\n specificingredient_id_and_calculated_amount \n')
    # pprint.pprint(specificingredient_id_and_calculated_amount)

    # Save the results to the database:
    for k in range(len(specificingredient_id_and_calculated_amount)):
        s = SpecificIngredient.objects.get(
            pk = specificingredient_id_and_calculated_amount[k]['id']
        )
        s.calculated_amount = \
        specificingredient_id_and_calculated_amount\
        [k]['calculated_amount']
        s.save()

    result_calculation_fulldayofeating = \
    query_result_calculation_fulldayofeating(id_fulldayofeating)

    context = {'id_fulldayofeating': id_fulldayofeating,
               'result_calculation_fulldayofeating': \
               result_calculation_fulldayofeating,
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

        rawingredient_k_queryset = RawIngredient.objects.filter(
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
