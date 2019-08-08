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
    MealplanForm
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class CreateMealplan(LoginRequiredMixin, CreateView):
    model = Mealplan
    fields = ['name',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListMealplan(
    LoginRequiredMixin,
    ListView
):
    model = Mealplan
    def get_queryset(self):
        return Mealplan.objects.filter(
            author = self.request.user
        ).order_by('name')


@login_required
def update_mealplan_view(request, id_mealplan):

    # Check if the user is the owner of the mealplan:
    author_id_user_request = request.user.id

    queryset_mealplan = Mealplan.objects.filter(id=id_mealplan).values()
    dict_mealplan = list(queryset_mealplan)[0]
    author_id_mealplan = dict_mealplan['author_id']

    user_did_author_mealplan = (author_id_user_request == author_id_mealplan)

    if not user_did_author_mealplan:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)

    form = MealplanForm()
    context = {'form': form,
               'user_did_author_mealplan': user_did_author_mealplan}
    # TODO: use reverse_lazy instead of hard coding the name of the html file.
    return render(request, 'measuredfood/mealplan_form.html', context)


class DetailMealplan(DetailView):
    model = Mealplan


class DeleteMealplan(DeleteView):
    model = Mealplan
    success_url = reverse_lazy('list-mealplan')

    def test_func(self):
        mealplan = self.get_object()
        if self.request.user == mealplan.author:
            return True
        return False
