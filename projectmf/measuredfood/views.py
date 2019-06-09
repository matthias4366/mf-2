from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'measuredfood/home.html')

# def home(request):
#     """
#     Building a minimal home view for the start.
#     """
#     return HttpResponse('<h1>Welcome to measured food.</h1>')
