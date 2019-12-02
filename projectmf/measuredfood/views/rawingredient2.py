# imports for the creation of user accounts
from django.shortcuts import render, redirect

# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
)
from measuredfood.models import (
    RawIngredient2
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from measuredfood.ingredient_properties2 import (
    VITAMINS_AND_DEFAULT_UNITS
)

from django.contrib.auth.decorators import login_required
from measuredfood.forms import RawIngredient2Form
from measuredfood.utils.check_if_author import check_if_author
import logging

from measuredfood.utils.error.custom_error import (
    UserIsNotAuthorError,
)

from ..forms import FoodDataCentralIDForm


@login_required
def create_rawingredient2(request):
    logging.info('My changed logging message.')
    """
    Create view for the RawIngredient2. RawIngredient2 is the updated version
    of RawIngredient.
    """
    if request.method == 'POST':
        form_rawingredient2 = RawIngredient2Form(request.POST)
        logging.info(form_rawingredient2.errors)
        if form_rawingredient2.is_valid():
            form_rawingredient2.instance.author = request.user
            form_rawingredient2.save()
            return redirect('list-rawingredient2')
        else:
            logging.info('form_rawingredient2 is not valid.')
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
            author=self.request.user
        ).order_by('name')


@login_required
def update_rawingredient2(request, id_rawingredient2):

    try:

        check_if_author(
            request,
            RawIngredient2,
            id_rawingredient2,
            UserIsNotAuthorError,
        )

        rawingredient2_object = RawIngredient2.objects.get(pk=id_rawingredient2)

        if request.method == 'POST':
            form_rawingredient2 = RawIngredient2Form(
                request.POST,
                instance=rawingredient2_object
            )
            if form_rawingredient2.is_valid():
                form_rawingredient2.save()
                return redirect('list-rawingredient2')
        else:
            form_rawingredient2 = RawIngredient2Form(
                instance=rawingredient2_object
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


class DeleteRawIngredient2(UserPassesTestMixin, DeleteView):
    model = RawIngredient2
    success_url = reverse_lazy('list-rawingredient2')

    def test_func(self):
        rawingredient2 = self.get_object()
        if self.request.user == rawingredient2.author:
            return True
        return False


# # TODO: delete this once the replacement code is done.
# @login_required
# def browse_rawingredient2(request):
#     context = {}
#     return render(request, 'measuredfood/rawingredient2_browse.html', context)


def get_from_food_data_central(request):
    """
    The user can search for an ingredient on FoodData Central, copy the FDC
    ID into the form and the ingredient will be added to the user's ingredients.

    This way, the users do not have to add their ingredients manually,
    which is so bothersome that it is unrealistic.
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FoodDataCentralIDForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('list-rawingredient2')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FoodDataCentralIDForm()

    context = {'form': form}
    return render(
        request,
        'measuredfood/rawingredient2_get_from_food_data_central.html',
        context)
