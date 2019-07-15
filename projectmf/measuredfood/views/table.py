from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import SpecificIngredientForm

# Create your views here.
def table(request):
    if request.method == 'POST':
        form = SpecificIngredientForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SpecificIngredientForm()
    return render(request, 'measuredfood/table.html', {'form': form})
