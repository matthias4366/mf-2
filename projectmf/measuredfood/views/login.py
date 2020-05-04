# from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.models import User
from measuredfood.models import UserProfile


def login_custom_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                user_object = User.objects.filter(username=username)
                user_profile_object = UserProfile.objects.filter(
                    user=user_object[0])
                user_has_completed_tutorial = \
                    getattr(user_profile_object[0], 'has_completed_tutorial')

                if user_has_completed_tutorial:
                    return redirect('list-fulldayofeating')
                else:
                    return redirect('nutrientprofile-make-for-user')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context_ = {"form": form}
    return render(request, 'measuredfood/login.html', context_)

