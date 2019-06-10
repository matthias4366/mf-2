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
    DeleteView,
    DetailView
)
from .models import RawIngredient
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .ingredient_properties import ALL_INGREDIENT_FIELD_NAMES

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
    fields = ALL_INGREDIENT_FIELD_NAMES

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListRawIngredients(
    LoginRequiredMixin,
    ListView
):
    model = RawIngredient
    ordering = ['name']


class UpdateRawIngredient(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RawIngredient
    fields = ALL_INGREDIENT_FIELD_NAMES

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False


class DetailRawIngredient(DetailView):
    model = RawIngredient


class DeleteRawIngredient(DeleteView):
    model = RawIngredient
    success_url = reverse_lazy('list-raw-ingredients')

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False
