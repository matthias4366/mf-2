from django.shortcuts import render
from django.http import HttpResponse

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# imports for the view to create raw ingredients
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import RawIngredient
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class CreateRawIngredient(LoginRequiredMixin, CreateView):
    model = RawIngredient
    fields = ['name', 'calories', 'fat', 'protein', 'carbohydrates']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# interim ingredient view. TODO remove and replace with proper class based view.
class ListRawIngredients(
    LoginRequiredMixin,
    # UserPassesTestMixin,  # TODO removed because it causes errors (missing
    # test function.) Fix error and then add it back in.
    ListView
):
    model = RawIngredient


class UpdateRawIngredient(
    # TODO Currently, it is probably possible for user A to edit the Ingredients
    # of user B. Make that impossible with the UserPassesTestMixin and by giving
    # the ingredients a foreignkey which contains who made them.
    LoginRequiredMixin,
    UpdateView
):
    pass
