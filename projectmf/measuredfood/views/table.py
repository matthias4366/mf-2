from django.shortcuts import render
from django.http import HttpResponse
import copy

# Create your views here.
def table(request):
    return render(request, 'measuredfood/table.html')
