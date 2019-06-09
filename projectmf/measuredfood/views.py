from django.shortcuts import render
from django.http import HttpResponse

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'measuredfood/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Your account has been created!' \
                             ' You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'measuredfood/register.html', {'form': form})
