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
from measuredfood.utils.check_if_author import check_if_author

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


class ListRawIngredient2(
    LoginRequiredMixin,
    ListView
):
    model = RawIngredient2
    def get_queryset(self):
        return RawIngredient2.objects.filter(
            author = self.request.user
        ).order_by('name')


@login_required
def update_rawingredient2(request, id_rawingredient2):
    user_is_author = check_if_author(
        request,
        RawIngredient2,
        id_rawingredient2
    )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)
    # The user is the author, proceed.

    rawingredient2_object = RawIngredient2.objects.get(pk=id_rawingredient2)

    if request.method == 'POST':
        form_rawingredient2 = RawIngredient2Form(
            request.POST,
            instance = rawingredient2_object
        )
        if form_rawingredient2.is_valid():
            form_rawingredient2.save()
            return redirect('list-rawingredient2')
    else:
        form_rawingredient2 = RawIngredient2Form(
            instance = rawingredient2_object
        )
        context = {
            'VITAMINS_AND_DEFAULT_UNITS': VITAMINS_AND_DEFAULT_UNITS,
            'form': form_rawingredient2
        }
        return render(
            request,
            'measuredfood/rawingredient2_form.html',
            context
            )

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
