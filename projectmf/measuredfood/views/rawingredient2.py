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
    RawIngredient2,
    NutrientProfile
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from measuredfood.ingredient_properties2 import (
    VITAMINS_AND_DEFAULT_UNITS
)

from django.contrib.auth.decorators import login_required
from measuredfood.forms import RawIngredient2Form

@login_required
def create_rawingredient2(request):
    """
    Create view for the RawIngredient2. RawIngredient2 is the updated version
    of RawIngredient.
    """
    if request.method == 'POST':
        form_rawingredient2 = RawIngredient2Form(request.POST)
        if form_rawingredient2.is_valid():
            form_rawingredient2.instance.author = request.user
            form_rawingredient2.save()
            return redirect('list-rawingredient2')
    else:
        form_rawingredient2 = RawIngredient2Form()
        context = {
            'VITAMINS_AND_DEFAULT_UNITS': VITAMINS_AND_DEFAULT_UNITS,
            'form': form_rawingredient2
        }
        return render(
            request,
            'measuredfood/rawingredient2_form.html',
            context
            )

class CreateRawIngredient2(LoginRequiredMixin, CreateView):
    model = RawIngredient2
    fields ='__all__'
    # success_url = reverse('list-rawingredient2')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateRawIngredient2, self).get_context_data(**kwargs)
        context['VITAMINS_AND_DEFAULT_UNITS'] = VITAMINS_AND_DEFAULT_UNITS
        return context

    def get_success_url(self):
        return reverse('list-rawingredient2')


class ListRawIngredient2(
    LoginRequiredMixin,
    ListView
):
    model = RawIngredient2
    def get_queryset(self):
        return RawIngredient2.objects.filter(
            author = self.request.user
        ).order_by('name')


class UpdateRawIngredient2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RawIngredient2
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False


class DetailRawIngredient2(UserPassesTestMixin, DetailView):
    model = RawIngredient2

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False

class DeleteRawIngredient2(UserPassesTestMixin, DeleteView):
    model = RawIngredient2
    success_url = reverse_lazy('list-raw-ingredients')

    def test_func(self):
        raw_ingredient = self.get_object()
        if self.request.user == raw_ingredient.author:
            return True
        return False
