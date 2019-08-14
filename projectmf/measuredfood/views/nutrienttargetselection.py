from django.contrib.auth.decorators import login_required
from measuredfood.forms import NutrientTargetSelectionForm
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from measuredfood.models import NutrientTargetSelection
from django.urls import reverse_lazy
from measuredfood.utils.check_if_author import check_if_author

@login_required
def create_nutrienttargetselection(request):
    if request.method == 'POST':
        form = NutrientTargetSelectionForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('list-nutrienttargetselection')
    else:
        form = NutrientTargetSelectionForm()
        context = {'form': form}
        return render(
            request,
            'measuredfood/nutrienttargetselection_form.html',
            context
            )

@login_required
def update_nutrienttargetselection(request, id_nutrienttargetselection):
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        NutrientTargetSelection,
        id_nutrienttargetselection
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)

    nutrienttargetselection_instance = NutrientTargetSelection.objects.get(
        pk = id_nutrienttargetselection
    )

    if request.method == 'POST':
        form = NutrientTargetSelectionForm(
            request.POST,
            instance = nutrienttargetselection_instance
        )
        if form.is_valid():
            form.save()
            return redirect(
                'list-nutrienttargetselection',
            )
    else:
        form = NutrientTargetSelectionForm(
            instance = nutrienttargetselection_instance
        )
        context = {'form': form}
        return render(
            request,
            'measuredfood/nutrienttargetselection_form.html',
            context
            )


class ListNutrientTargetSelection(
    LoginRequiredMixin,
    ListView
):
    model = NutrientTargetSelection
    def get_queryset(self):
        return NutrientTargetSelection.objects.filter(
            author = self.request.user
        ).order_by('name')


class DetailNutrientTargetSelection(UserPassesTestMixin, DetailView):
    model = NutrientTargetSelection

    def test_func(self):
        nutrienttargetselection_ = self.get_object()
        if self.request.user == nutrienttargetselection_.author:
            return True
        return False


class DeleteNutrientTargetSelection(UserPassesTestMixin, DeleteView):
    model = NutrientTargetSelection
    success_url = reverse_lazy('list-nutrienttargetselection')

    def test_func(self):
        nutrienttargetselection_ = self.get_object()
        if self.request.user == nutrienttargetselection_.author:
            return True
        return False
