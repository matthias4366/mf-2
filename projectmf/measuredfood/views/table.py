from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import SpecificIngredientForm

# The primary key pk is from the fulldayofeating.
def table(request, pk):

    # get the fulldayofeating based on its pk
    

    if request.method == 'POST':
        form = SpecificIngredientForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SpecificIngredientForm()
    return render(request, 'measuredfood/table.html', {'form': form})
