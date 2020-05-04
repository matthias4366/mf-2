# from django.http import request
from django.shortcuts import render, redirect


def login_custom_view(request):
    context_ = {}
    return render(request, 'measuredfood/login.html', context_)

