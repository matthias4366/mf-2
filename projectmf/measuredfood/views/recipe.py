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
    Recipe
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_ALL,
    INGREDIENT_FIELDS_NUTRITION
)


class CreateRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListRecipes(
    LoginRequiredMixin,
    ListView
):
    model = Recipe
    ordering = ['name']


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class DetailRecipe(DetailView):
    model = Recipe


class DeleteRecipe(DeleteView):
    model = Recipe
    success_url = reverse_lazy('list-recipes')

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False
