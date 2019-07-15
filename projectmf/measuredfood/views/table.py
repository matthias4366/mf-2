from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import copy

from measuredfood.forms import NameForm

# Create your views here.
def table(request):
    return render(request, 'measuredfood/table.html')
