# import pprint
# import json
# imports for the creation of user accounts
import re
from django.shortcuts import render, redirect

# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
)
from measuredfood.models import (
    RawIngredient3,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from measuredfood.forms import RawIngredient3Form
from measuredfood.utils.check_if_author import check_if_author
from measuredfood.utils.rawingredient3.\
    transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood
import logging

from measuredfood.utils.error.custom_error import (
    UserIsNotAuthorError,
    FoodDataCentralAPIResponseError,
)

from measuredfood.utils.rawingredient3.\
    calculate_carbohydrate_without_fiber_model_instance import \
    calculate_carbohydrate_without_fiber_model_instance

from ..forms import FoodDataCentralIDForm
from ..utils.rawingredient3.make_rawingredient3_from_usda_data import \
    make_rawingredient3_from_usda_data
from ..utils.rawingredient3.rename_duplicate import \
    rename_duplicate
from ..utils.set_to_zero_if_none import set_to_zero_if_none

import requests


@login_required
def create_rawingredient3(request):
    logging.info('My changed logging message.')
    """
    Create view for the RawIngredient3. RawIngredient3 is the updated version
    of RawIngredient2.
    """
    if request.method == 'POST':
        form_rawingredient3 = RawIngredient3Form(request.POST)
        logging.info(form_rawingredient3.errors)
        if form_rawingredient3.is_valid():
            form_rawingredient3.instance.author = request.user

            form_rawingredient3.save()

            rename_duplicate(
                RawIngredient3,
                'name',
                request.user,
                re,
            )

            return redirect('list-rawingredient3')
        else:
            logging.info('form_rawingredient3 is not valid.')
    else:
        form_rawingredient3 = RawIngredient3Form()
        context = {
            'form': form_rawingredient3
        }
        return render(
            request,
            'measuredfood/rawingredient3_form.html',
            context
            )


class ListRawIngredient3(
    LoginRequiredMixin,
    ListView
):
    model = RawIngredient3

    def get_queryset(self):
        return RawIngredient3.objects.filter(
            author=self.request.user
        ).order_by('name')


class DetailRawIngredient3(DetailView):
    model = RawIngredient3


@login_required
def update_rawingredient3(request, id_rawingredient3):

    try:

        check_if_author(
            request,
            RawIngredient3,
            id_rawingredient3,
            UserIsNotAuthorError,
        )

        rawingredient3_object = RawIngredient3.objects.get(
            pk=id_rawingredient3
        )

        if request.method == 'POST':
            form_rawingredient3 = RawIngredient3Form(
                request.POST,
                instance=rawingredient3_object
            )
            if form_rawingredient3.is_valid():
                form_rawingredient3.save()
                return redirect('list-rawingredient3')
        else:
            form_rawingredient3 = RawIngredient3Form(
                instance=rawingredient3_object
            )
            context = {
                'form': form_rawingredient3
            }
            return render(
                request,
                'measuredfood/rawingredient3_form.html',
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


class DeleteRawIngredient3(UserPassesTestMixin, DeleteView):
    model = RawIngredient3
    success_url = reverse_lazy('list-rawingredient3')

    def test_func(self):
        rawingredient3 = self.get_object()
        if self.request.user == rawingredient3.author:
            return True
        return False


@login_required()
def get_from_food_data_central(request):
    """
    The user can search for an ingredient on FoodData Central, copy the FDC
    ID into the form and the ingredient will be added to the user's ingredients.

    This way, the users do not have to add their ingredients manually,
    which is so bothersome that it is unrealistic.

    Built for RawIngredient3.
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FoodDataCentralIDForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Getting the fdc_id the user typed in.
            fdc_id = form.cleaned_data['FDC_ID']

            # TODO: Move the API Key into a environment variable.
            # API Key for tailoredmealplans@gmail.com.
            api_key = 'yucJ7dnpJ85gj5bFGg0RK463TZqb9gu2Gy4vvCDd'

            url_food_details = r'https://api.nal.usda.gov/fdc/v1/' \
                               + fdc_id \
                               + r'?api_key=' \
                               + api_key

            try:
                response = requests.get(
                    url_food_details,
                )
                response_json = response.json()

                # Check if there was an error in the API reponse.
                if 'status' in response_json:
                    raise FoodDataCentralAPIResponseError(response_json)

                rawingredient3_instance = make_rawingredient3_from_usda_data(
                    RawIngredient3,
                    request,
                    response_json,
                    transform_nutrient_name_usda_to_measuredfood,
                )

                rawingredient3_instance = \
                    calculate_carbohydrate_without_fiber_model_instance(
                        rawingredient3_instance,
                        set_to_zero_if_none,
                    )

                rawingredient3_instance.save()

                rename_duplicate(
                    RawIngredient3,
                    'name',
                    request.user,
                    re,
                )

                return redirect('list-rawingredient3')

            except FoodDataCentralAPIResponseError:

                context = {
                    'error_message':
                        'An error has occured while accessing the FoodData '
                        'Central API. Did you enter a valid FDC ID? They are '
                        'six digit numbers, for example 548596. Another '
                        'possible reason is that the API is receiving too '
                        'many requests, which is something the developers '
                        'need to fix. You, the user, can not do much except '
                        'maybe try again later.',
                    'error_id': 'FoodDataCentralAPIResponseError',
                }
                return render(
                    request,
                    'measuredfood/error/general_error_page.html',
                    context
                )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FoodDataCentralIDForm()

    context = {'form': form}
    return render(
        request,
        'measuredfood/rawingredient3_get_from_food_data_central.html',
        context)
