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
    Mealplan,
    FullDayOfEating
)
from measuredfood.forms import (
    MealplanForm,
    SpecificFullDayOfEatingFormset
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from measuredfood.utils.check_if_author import check_if_author

class CreateMealplan(LoginRequiredMixin, CreateView):
    model = Mealplan
    fields = ['name',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def update_mealplan_view(request, id_mealplan):
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        Mealplan,
        id_mealplan
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)
    # The user is the author, proceed.

    mealplan_object = Mealplan.objects.get(pk = id_mealplan)

    if request.method == 'POST':
        form_mealplan = MealplanForm(
            request.POST,
            instance = mealplan_object
        )
        formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
            request.POST,
            instance = mealplan_object
        )
        
        if form_mealplan.is_valid() and \
        formset_specificfulldayofeating.is_valid():
            formset_specificfulldayofeating.save()
            form_mealplan.save()
            return redirect(
                'update-mealplan',
                id_mealplan=mealplan_object.id
                )
    else:
        form_mealplan = MealplanForm(instance = mealplan_object)
        formset_specificfulldayofeating = SpecificFullDayOfEatingFormset(
            instance = mealplan_object
        )
        # Only let the user select FullDayOfEating objects from their own
        # collection.
        for form in formset_specificfulldayofeating:
            form.fields['fulldayofeating'].queryset = \
            FullDayOfEating.objects.filter(
                author = request.user.id
            )

        context = {
            'form_mealplan': form_mealplan,
            'formset_specificfulldayofeating': formset_specificfulldayofeating
        }
        # TODO: use reverse_lazy instead of hard coding the name of the html file.
        return render(request, 'measuredfood/mealplan_form.html', context)


class ListMealplan(
    LoginRequiredMixin,
    ListView
):
    model = Mealplan
    def get_queryset(self):
        return Mealplan.objects.filter(
            author = self.request.user
        ).order_by('name')


class DetailMealplan(UserPassesTestMixin, DetailView):
    model = Mealplan

    def test_func(self):
        mealplan = self.get_object()
        if self.request.user == mealplan.author:
            return True
        return False


class DeleteMealplan(UserPassesTestMixin, DeleteView):
    model = Mealplan
    success_url = reverse_lazy('list-mealplan')

    def test_func(self):
        mealplan = self.get_object()
        if self.request.user == mealplan.author:
            return True
        return False
