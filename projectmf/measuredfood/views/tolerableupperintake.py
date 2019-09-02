from django.contrib.auth.decorators import login_required
from measuredfood.models import TolerableUpperIntake
from measuredfood.forms import TolerableUpperIntakeForm
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from measuredfood.utils.check_if_author import check_if_author
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


@login_required
def update_tolerableupperintake_view(request, id_tolerableupperintake):
    # Make sure users can not edit other user's objects.
    user_is_author = check_if_author(
        request,
        TolerableUpperIntake,
        id_tolerableupperintake
        )
    if not user_is_author:
        context = {}
        return render(request, 'measuredfood/not_yours.html', context)

    instance_tolerableupperintake = TolerableUpperIntake.objects.get(
        pk=id_tolerableupperintake
        )

    if request.method == 'POST':
        form = TolerableUpperIntakeForm(
            request.POST,
            instance=instance_tolerableupperintake
            )
        if form.is_valid():
            form.save()
            return redirect(
                'list-tolerableupperintake',
                )
    else:
        form = TolerableUpperIntakeForm(
            instance=instance_tolerableupperintake
            )
        context = {'form': form}
        return render(
            request,
            'measuredfood/tolerableupperintake_form.html',
            context
            )


@login_required
def create_tolerableupperintake_view(request):
    if request.method == 'POST':
        form = TolerableUpperIntakeForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('list-tolerableupperintake')
    else:
        form = TolerableUpperIntakeForm()
        context = {'form': form}
        return render(
            request,
            'measuredfood/tolerableupperintake_form.html',
            context
            )


class ListTolerableUpperIntake(
    LoginRequiredMixin,
    ListView
):
    model = TolerableUpperIntake

    def get_queryset(self):
        return TolerableUpperIntake.objects.filter(
            author=self.request.user
        ).order_by('name')


class DetailTolerableUpperIntake(UserPassesTestMixin, DetailView):
    model = TolerableUpperIntake

    def test_func(self):
        tolerableupperintake_ = self.get_object()
        if self.request.user == tolerableupperintake_.author:
            return True
        return False


class DeleteTolerableUpperIntake(UserPassesTestMixin, DeleteView):
    model = TolerableUpperIntake
    success_url = reverse_lazy('list-tolerableupperintake')

    def test_func(self):
        tolerableupperintake_ = self.get_object()
        if self.request.user == tolerableupperintake_.author:
            return True
        return False
