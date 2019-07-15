from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import SpecificIngredientForm

from measuredfood.models import FullDayOfEating, SpecificIngredient

def table(request, id_fulldayofeating):

    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)

    specificingredient_queryset = SpecificIngredient.objects.filter(fulldayofeating__id=id_fulldayofeating)
    print(specificingredient_queryset)

    if request.method == 'POST':
        form = SpecificIngredientForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SpecificIngredientForm()
    return render(
        request,
        'measuredfood/table.html',
        {'form': form,
         'fulldayofeating': fulldayofeating_object,
         'specificingredient_queryset': specificingredient_queryset})
