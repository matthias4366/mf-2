from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import (
    SpecificIngredientForm,
    FullDayOfEatingForm,
    )

from measuredfood.models import FullDayOfEating, SpecificIngredient

from django.forms import modelformset_factory, inlineformset_factory

def table(request, id_fulldayofeating):
    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)
    SpecificIngredientFormset = inlineformset_factory(FullDayOfEating, SpecificIngredient, fields=('__all__'), extra=1)

    if request.method == 'POST':
        form_fulldayofeating = FullDayOfEatingForm(request.POST, instance=fulldayofeating_object)
        formset = SpecificIngredientFormset(request.POST, instance=fulldayofeating_object)
        if formset.is_valid():
            formset.save()
            return redirect('update-fulldayofeating', id_fulldayofeating=fulldayofeating_object.id)
    else:
        form_fulldayofeating = FullDayOfEatingForm(instance=fulldayofeating_object)
        formset = SpecificIngredientFormset(instance=fulldayofeating_object)
        print(formset[0].fields)
        context = {'formset': formset,
                   'form_fulldayofeating': form_fulldayofeating,}
        return render(request,'measuredfood/table.html', context)
