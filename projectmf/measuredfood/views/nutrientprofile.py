from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from measuredfood.models import (NutrientProfile)
from measuredfood.forms import (NutrientProfileForm)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from measuredfood.utils.check_if_author import check_if_author
from measuredfood.utils.error.custom_error import (
    UserIsNotAuthorError,
)


@login_required
def update_nutrientprofile(request, id_nutrientprofile):
    try:
        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            NutrientProfile,
            id_nutrientprofile,
            UserIsNotAuthorError,
            )

        instance_nutrientprofile = NutrientProfile.objects.get(
            pk=id_nutrientprofile
            )

        if request.method == 'POST':
            form = NutrientProfileForm(
                request.POST,
                instance=instance_nutrientprofile
                )
            if form.is_valid():
                form.save()
                return redirect(
                    'list-nutrient-profiles',
                    )
        else:
            form = NutrientProfileForm(
                instance=instance_nutrientprofile
                )
            context = {'form': form}
            return render(
                request,
                'measuredfood/nutrientprofile_form.html',
                context
                )

    except UserIsNotAuthorError:
            """
            Careful when you implement this. You will have to make changes at 
            multiple spots in the code.
            """
            context = {
                'error_message': 'It seems like you are trying to edit an object '
                                 'of another user, which is forbidden.',
                'error_id': 'UserIsNotAuthorError',
            }
            return render(
                request,
                'measuredfood/error/general_error_page.html',
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
            author=self.request.user
        ).order_by('name')


class DetailNutrientProfile(DetailView):
    model = NutrientProfile


class DeleteNutrientProfile(UserPassesTestMixin, DeleteView):
    model = NutrientProfile
    success_url = reverse_lazy('list-nutrient-profiles')

    def test_func(self):
        nutrient_profile_ = self.get_object()
        if self.request.user == nutrient_profile_.author:
            return True
        return False


def copy_nutrientprofile_to_user(request, id_nutrientprofile):
    """
    From the publicly available full days of eating, copy a full day of
    eating to the user's full day of eating objects.
    :return:
    """

    # Copy the NutrientProfile.
    nutrient_profile_copy = NutrientProfile.objects.get(
        id=id_nutrientprofile
    )
    nutrient_profile_copy.pk = None
    nutrient_profile_copy.author = request.user
    nutrient_profile_copy.save()

    nutrientprofile_list = NutrientProfile.objects.filter(
        author=request.user
    ).order_by('name')

    context = {'nutrientprofile_list': nutrientprofile_list}

    return render(
        request,
        'measuredfood/nutrientprofile_list.html',
        context
    )
