from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import (
    SpecificIngredientForm,
    FullDayOfEatingForm,
    )

from measuredfood.models import FullDayOfEating, SpecificIngredient

def table(request, id_fulldayofeating):

    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)

    specificingredient_queryset = SpecificIngredient.objects.filter(fulldayofeating__id=id_fulldayofeating)

    # This form collects all the forms for the specific ingredients that need
    # to be displayed in the template.
    form_specificingredient_list = []

    if request.method == 'POST':

        form = SpecificIngredientForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation

        form_fulldayofeating = FullDayOfEatingForm(request.POST, instance=fulldayofeating_object)
    else:
        form_fulldayofeating = FullDayOfEatingForm(instance=fulldayofeating_object)

        form = SpecificIngredientForm()

    return render(
        request,
        'measuredfood/table.html',
        {
            'form_fulldayofeating': form_fulldayofeating,
            'form': form,
         })
