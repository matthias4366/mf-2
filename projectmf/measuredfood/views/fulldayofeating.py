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
        # needed, do not delete
        queryset_specificingredient = SpecificIngredient.objects.filter(
            fulldayofeating_id=id_fulldayofeating
            )
        # needed
        list_specificingredient_id = [
            s.id for s in queryset_specificingredient
            ]

        # Get the information about the specific ingredients belonging to the
        # fulldayofeating
        # needed, do not delete
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
