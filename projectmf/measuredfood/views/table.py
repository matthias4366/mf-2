from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import SpecificIngredientForm

from measuredfood.models import FullDayOfEating

# The primary key pk is from the fulldayofeating.
def table(request, id_fulldayofeating):

    # get the fulldayofeating based on its pk
    print('\n\n\n\n\n')
    print('Name of the FullDayOfEating:')
    print(f'{FullDayOfEating.objects.get(pk=id_fulldayofeating).name}')
    print('\n\n\n\n\n')

    fulldayofeating_object = FullDayOfEating.objects.get(pk=id_fulldayofeating)

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
         'fulldayofeating': fulldayofeating_object})
