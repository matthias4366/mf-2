from django.shortcuts import render
from django.http import HttpResponse
import copy

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# imports for the view to create raw ingredients
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)
from .models import (
    RawIngredient,
    NutrientProfile
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .ingredient_properties import (
    INGREDIENT_FIELDS_ALL,
    INGREDIENT_FIELDS_NUTRITION
)

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
    fields = INGREDIENT_FIELDS_ALL

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
    fields = INGREDIENT_FIELDS_ALL

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

# Nutrient profiles

class CreateNutrientProfile(LoginRequiredMixin, CreateView):
    model = NutrientProfile
    all_fields = copy.deepcopy(INGREDIENT_FIELDS_NUTRITION)
    all_fields.insert(0, 'name')
    fields = all_fields

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListNutrientProfile(
    LoginRequiredMixin,
    ListView
):
    model = NutrientProfile
    ordering = ['name']


class UpdateNutrientProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NutrientProfile
    fields = INGREDIENT_FIELDS_NUTRITION

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        nutrient_profile_ = self.get_object()
        if self.request.user == nutrient_profile_.author:
            return True
        return False


class DetailNutrientProfile(DetailView):
    model = NutrientProfile


class DeleteNutrientProfile(DeleteView):
    model = NutrientProfile
    success_url = reverse_lazy('list-nutrient-profiles')

    def test_func(self):
        nutrient_profile_ = self.get_object()
        if self.request.user == nutrient_profile_.author:
            return True
        return False


# Specific Ingredient
