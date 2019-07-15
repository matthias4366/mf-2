from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import RawIngredientForm

# Create your views here.
def table(request):
    if request.method == 'POST':
        form = RawIngredientForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = RawIngredientForm()
    return render(request, 'measuredfood/table.html', {'form': form})
