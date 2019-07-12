from django.shortcuts import render
from django.http import HttpResponse
import copy

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from measuredfood.forms import UserRegisterForm

# imports for the view to create raw ingredients
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)
from measuredfood.models import (
    RawIngredient,
    NutrientProfile
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_ALL,
    INGREDIENT_FIELDS_NUTRITION
)


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
