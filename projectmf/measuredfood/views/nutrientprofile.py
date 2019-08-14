from django.shortcuts import render
from django.http import HttpResponse
import copy

# imports for the creation of user accounts
from django.shortcuts import render, redirect
from django.contrib import messages
from measuredfood.forms import UserRegisterForm

# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from measuredfood.models import (NutrientProfile)
from measuredfood.forms import (NutrientProfileForm)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_ALL,
    INGREDIENT_FIELDS_NUTRITION
)
from django.contrib.auth.decorators import login_required
from measuredfood.utils.check_if_author import check_if_author

@login_required
def update_nutrientprofile(request, id_nutrientprofile):
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        NutrientProfile,
        id_nutrientprofile
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)

    instance_nutrientprofile = NutrientProfile.objects.get(
        pk=id_nutrientprofile
        )

    if request.method == 'POST':
        form = NutrientProfileForm(
            request.POST,
            instance = instance_nutrientprofile
            )
        if form.is_valid():
            form.save()
            return redirect(
                'list-nutrient-profiles',
                )
    else:
        form = NutrientProfileForm(
            instance = instance_nutrientprofile
            )
        context = {'form': form}
        return render(
            request,
            'measuredfood/nutrientprofile_form.html',
            context
            )

@login_required
def create_nutrientprofile(request):
    if request.method == 'POST':
        form = NutrientProfileForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('list-nutrient-profiles')
    else:
        form = NutrientProfileForm()
        context = {'form': form}
        return render(
            request,
            'measuredfood/nutrientprofile_form.html',
            context
            )

class ListNutrientProfile(
    LoginRequiredMixin,
    ListView
):
    model = NutrientProfile
    def get_queryset(self):
        return NutrientProfile.objects.filter(
            author = self.request.user
        ).order_by('name')


class DetailNutrientProfile(UserPassesTestMixin, DetailView):
    model = NutrientProfile

    def test_func(self):
        nutrient_profile_ = self.get_object()
        if self.request.user == nutrient_profile_.author:
            return True
        return False

class DeleteNutrientProfile(UserPassesTestMixin, DeleteView):
    model = NutrientProfile
    success_url = reverse_lazy('list-nutrient-profiles')

    def test_func(self):
        nutrient_profile_ = self.get_object()
        if self.request.user == nutrient_profile_.author:
            return True
        return False
