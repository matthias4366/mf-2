# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from measuredfood.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Your account has been created!'
                             ' You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'measuredfood/register.html', {'form': form})
