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
                id_mealplan = mealplan_object.id
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
            'formset_specificfulldayofeating': formset_specificfulldayofeating,
            'id_mealplan': mealplan_object.id
        }
        # TODO: use reverse_lazy instead of hard coding the name of the html file.
        return render(request, 'measuredfood/mealplan_form.html', context)

@login_required
def shoppinglist_view(request, id_mealplan):
    # From id_mealplan, get all the related SpecificFullDayOfEating objects.

    # From all the SpecificFullDayOfEating, get the related FullDayOfEating
    # objects. Save the id values in a list. Make two lists: one without
    # duplications for the recalculation and one with duplications for the
    # making of the shopping list.

    # Iterate through the id_list_no_duplications and recalculate the amounts
    # for every FullDayOfEating in that list. Write a separate function for
    # that which just takes in the id of the FullDayOfEating and does
    # everything else on its own.

    # Sum up the calculated amounts.
    # Initiate a dictionary shopping_list_dict which will have the format
    # {'RawIngredient_name': sum total amount}
    # Iterate over the id_list_with_duplications. For each FullDayOfEating in
    # that list, iterate over all the SpecificIngredients.
    # For each SpecificIngredient, get the name of the associated RawIngredient.
    # Check if the name of the RawIngredient is already in the
    # shopping_list_dict. If it is not, add it and initialize the sum total
    # amount as 0.
    # After that, add the calculated_amount of the SpecificIngredient which
    # is related to the RawIngredient to the sum total amount. 



    context = {}
    return render(request, 'measuredfood/shoppinglist.html', context)


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
