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
        result_mockup_string = 'Your results will be displayed here.'
        result_mockup_ingredient_list_0 = SpecificIngredient.objects.filter(
            fulldayofeating__id=id_fulldayofeating
            ).values('rawingredient_id')
        print('\n\n\n\n')
        print(result_mockup_ingredient_list_0)
        print('\n\n\n\n')
        result_mockup_ingredient_list = list(
            RawIngredient.objects.filter(
            id=1).values('name')
            )
        print('\n\n\n\n')
        print(result_mockup_ingredient_list)
        print('\n\n\n\n')
        context = {'formset': formset,
                   'form_fulldayofeating': form_fulldayofeating,
                   'id_fulldayofeating': id_fulldayofeating,
                   'result_calculation_fulldayofeating': result_mockup_string
                   }
        # TODO: use reverse function instead
        return render(request,'measuredfood/fulldayofeating_calculate.html', context)
