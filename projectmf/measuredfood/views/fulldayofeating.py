from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import copy
from measuredfood.forms import (
    SpecificIngredientForm,
    FullDayOfEatingForm,
    )
from measuredfood.models import (
    RawIngredient
)
from measuredfood.models import FullDayOfEating, SpecificIngredient
from django.forms import modelformset_factory, inlineformset_factory
from django.urls import reverse, reverse_lazy
# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def create_fulldayofeating(request):
    """
    Largely copied from the update_fulldayofeating function. Always edit that
    function first and copy the changes to the create_fulldayofeating function.
    """

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(request.POST)
        if form_fulldayofeating.is_valid():
            form_fulldayofeating.instance.author = request.user
            form_fulldayofeating.save()
            return redirect('list-fulldayofeating')
    else:
        form_fulldayofeating = FullDayOfEatingForm()
        context = {'form_fulldayofeating': form_fulldayofeating}
        return render(
            request,
            'measuredfood/fulldayofeating_create.html',
            context
            )


def update_fulldayofeating(request, id_fulldayofeating):
    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)
    SpecificIngredientFormset = inlineformset_factory(
        FullDayOfEating,
        SpecificIngredient,
        fields=('__all__'),
        extra=1
        )

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(
            request.POST,
            instance=fulldayofeating_object
            )
        formset = SpecificIngredientFormset(
            request.POST,
            instance=fulldayofeating_object
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
            instance=fulldayofeating_object
            )
        formset = SpecificIngredientFormset(instance=fulldayofeating_object)
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
    ordering = ['name']


class DetailFullDayOfEating(DetailView):
    model = FullDayOfEating


class DeleteFullDayOfEating(DeleteView):
    model = FullDayOfEating
    success_url = reverse_lazy('list-fulldayofeating')

    def test_func(self):
        fulldayofeating_ = self.get_object()
        if self.request.user == fulldayofeating_.author:
            return True
        return False


def calculate_fulldayofeating(request, id_fulldayofeating):
    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)
    SpecificIngredientFormset = inlineformset_factory(
        FullDayOfEating,
        SpecificIngredient,
        fields=('__all__'),
        extra=1
        )

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(
            request.POST,
            instance=fulldayofeating_object
            )
        formset = SpecificIngredientFormset(
            request.POST,
            instance=fulldayofeating_object
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
            instance=fulldayofeating_object
            )
        formset = SpecificIngredientFormset(instance=fulldayofeating_object)

        """
        In the page fulldayofeating_calculate.html, at the bottom, a table
        should display the results of the calculation. Here, the results are
        queried and given to the context dictionary.
        """
        # Get the names of the raw ingredients belonging to the fulldayofeating
        queryset_specificingredient = SpecificIngredient.objects.filter(
            fulldayofeating_id=id_fulldayofeating
            )
        list_rawingredient_id = [
            s.rawingredient_id for s in queryset_specificingredient
            ]
        queryset_rawingredient = RawIngredient.objects.filter(
            id__in = list_rawingredient_id
            )
        list_of_dict_rawingredient = list(queryset_rawingredient.values())

        # Get the information about the specific ingredients belonging to the
        # fulldayofeating
        list_of_dict_specificingredient = list(
            queryset_specificingredient.values()
            )
        list_of_dict_specificingredient_len = len(
            list_of_dict_specificingredient
            )

        result_calculation_fulldayofeating_mockup = [
            {'calculated_amount': 200,
             'base_amount_unit': 'g',
             'name': 'Pea protein powder',
             'buy_here_link': 'www.proteinshop.com'},
            {'calculated_amount': 400,
             'base_amount_unit': 'g',
             'name': 'Pasta',
             'buy_here_link': 'www.pastashop.com'},

        ]

        """There are two lists of dictionaries, one for the RawIngredient and
        one for the SpecificIngredient. The n-th dictionaries in both lists are
        to be merged. The result should be a list of merged dictionaries.
        How to merge python dictionaries: z = {**x, **y}."""
        result_calculation_fulldayofeating = []
        if len(list_of_dict_specificingredient) == len(list_of_dict_rawingredient):
            for k in range(len(list_of_dict_specificingredient)):
                merged_dict_k = {**list_of_dict_specificingredient[k], **list_of_dict_rawingredient[k]}
                result_calculation_fulldayofeating.append(merged_dict_k)
        else:
            print('\n\n ERROR: The dictionaries for the RawIngredient and the\
                  SpecificIngredient do not have the same length! \n\n')

        print('\n\n')
        print('result_calculation_fulldayofeating')
        print(result_calculation_fulldayofeating)

        context = {'formset': formset,
                   'form_fulldayofeating': form_fulldayofeating,
                   'id_fulldayofeating': id_fulldayofeating,
                   'result_calculation_fulldayofeating': \
                   result_calculation_fulldayofeating,
                   }
        # TODO: use reverse function instead
        return render(request,'measuredfood/fulldayofeating_calculate.html', context)
