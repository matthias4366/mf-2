from django.shortcuts import render
from django.http import HttpResponse
import copy

# Create your views here.
def home(request):
    return render(request, 'measuredfood/home.html')
