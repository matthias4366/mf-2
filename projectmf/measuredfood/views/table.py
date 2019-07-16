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
    list_of_forms_specificingredient = []

    if request.method == 'POST':
        # Full day of eating
        form_fulldayofeating = FullDayOfEatingForm(request.POST, instance=fulldayofeating_object)
        if form_fulldayofeating.is_valid():
            form_fulldayofeating.save()

        # Specific Ingredient # TODO code this part.

    else:
        # Full day of eating
        form_fulldayofeating = FullDayOfEatingForm(instance=fulldayofeating_object)

        # Specific Ingredient
        for i in specificingredient_queryset:
            form_specificingredient_i = SpecificIngredientForm(instance = i)
            list_of_forms_specificingredient.append(form_specificingredient_i)

    return render(
        request,
        'measuredfood/table.html',
        {
            'form_fulldayofeating': form_fulldayofeating,
            'list_of_forms_specificingredient': list_of_forms_specificingredient,
         })
