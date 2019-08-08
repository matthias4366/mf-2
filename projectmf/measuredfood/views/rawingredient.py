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
    def get_queryset(self):
        return RawIngredient.objects.filter(
            author = self.request.user
        ).order_by('name')


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


class DetailRawIngredient(UserPassesTestMixin, DetailView):
    model = RawIngredient
    
    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False

class DeleteRawIngredient(UserPassesTestMixin, DeleteView):
    model = RawIngredient
    success_url = reverse_lazy('list-raw-ingredients')

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False
