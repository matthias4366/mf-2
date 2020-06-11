from django.shortcuts import render, redirect
from measuredfood.forms import (
    FullDayOfEating2Form,
    SpecificIngredient2Formset
    )
from measuredfood.models import (
    RawIngredient3,
    NutrientProfile,
    SpecificIngredient2,
    FullDayOfEating2,
)
from django.urls import reverse_lazy
# imports for the view to create raw ingredients
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from measuredfood.utils.check_if_author import check_if_author

from measuredfood.utils.error.custom_error import (
    UserIsNotAuthorError,
)

from measuredfood.utils.fulldayofeating2\
    .query_input_and_calculate_fulldayofeating2 \
    import query_input_and_calculate_fulldayofeating2

from measuredfood.utils.fulldayofeating2.query_ingredients_fulldayofeating2 \
    import query_ingredients_fulldayofeating2

import pprint

from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
)

from measuredfood.utils.set_to_zero_if_none\
    import set_to_zero_if_none

from measuredfood.utils.fulldayofeating2\
    .query_nutrientprofile_of_fulldayofeating2 \
    import query_nutrientprofile_of_fulldayofeating2

from measuredfood.utils.fulldayofeating2.calculate_fulldayofeating2 \
    import calculate_fulldayofeating2

from measuredfood.utils.fulldayofeating2\
    .calculate_average_of_specificingredient2_group \
    import calculate_average_of_specificingredient2_group

from measuredfood.utils.fulldayofeating2\
    .make_list_variable_ingredient_and_group \
    import make_list_variable_ingredient_and_group

from measuredfood.utils.fulldayofeating2\
    .calculate_specificingredient2_amount_try \
    import calculate_specificingredient2_amount_try

from measuredfood.utils.error.custom_error import \
    NumberTargetedNutrientsNotEqualNumberScalingEntitiesError

from measuredfood.utils.fulldayofeating2.\
    undo_calculate_average_of_specificingredient2_group \
    import undo_calculate_average_of_specificingredient2_group

from measuredfood.utils.fulldayofeating2\
    .make_specificingredient2_id_and_calculated_amount_dict import \
    make_specificingredient2_id_and_calculated_amount_dict

from measuredfood.utils.fulldayofeating2\
    .save_fulldayofeating2_calculation_result_to_database import \
    save_fulldayofeating2_calculation_result_to_database

from measuredfood.utils.fulldayofeating2\
    .prepare_calculation_result_for_display import \
    prepare_calculation_result_for_display

from measuredfood.utils.fulldayofeating2\
    .make_aggregated_total_nutrition import \
    make_aggregated_total_nutrition

from measuredfood.utils.fulldayofeating2\
    .calculate_total_nutrition_fulldayofeating2 import \
    calculate_total_nutrition_fulldayofeating2

from measuredfood.utils.fulldayofeating2\
    .calculate_percentage_of_target_amount import \
    calculate_percentage_of_target_amount

from measuredfood.utils.fulldayofeating2\
    .calculate_percent_max_fulldayofeating import \
    calculate_percent_max_fulldayofeating

from measuredfood.utils.fulldayofeating2\
    .judge_total_nutrition import \
    judge_total_nutrition

import copy
import numpy as np
import logging

logger_fulldayofeating2 = logging.getLogger(__name__)
logger_fulldayofeating2.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('fulldayofeating2.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger_fulldayofeating2.addHandler(file_handler)

from measuredfood.utils.error.custom_error \
    import NoValueForTargetedNutrientError


@login_required
def create_fulldayofeating2_view(request):
    """
    The FullDayOfEating2 has to first be created and saved to the database.
    Afterwards, the SpecificIngredient2 objects can be created; since they
    are related to the FullDayOfEating2 object.
    """

    if request.method == 'POST':
        form_fulldayofeating2 = FullDayOfEating2Form(
            request.user.id, request.POST
        )
        if form_fulldayofeating2.is_valid():
            form_fulldayofeating2.instance.author = request.user
            new_fulldayofeating = form_fulldayofeating2.save()
            return redirect(
                'update-fulldayofeating2',
                id_fulldayofeating2=new_fulldayofeating.id
            )
    else:
        form_fulldayofeating2 = FullDayOfEating2Form(request.user.id)
        context = {'form_fulldayofeating2': form_fulldayofeating2}
        return render(
            request,
            'measuredfood/fulldayofeating2_create.html',
            context
            )


@login_required
def update_fulldayofeating2_view(request, id_fulldayofeating2):

    try:

        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating2,
            id_fulldayofeating2,
            UserIsNotAuthorError
            )

        fulldayofeating2_object = FullDayOfEating2.objects.get(
            pk=id_fulldayofeating2
        )

        if request.method == 'POST':
            form_fulldayofeating2 = FullDayOfEating2Form(
                request.user.id,
                request.POST,
                instance=fulldayofeating2_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # That is because of how the FullDayOfEating2Form is set up.
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating2.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient2 = SpecificIngredient2Formset(
                request.POST,
                instance=fulldayofeating2_object
                )
            # I do not know if this part is necessary. It seems to work without.
            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient2:
                form.fields['rawingredient3'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            if formset_specificingredient2.is_valid() \
                    and form_fulldayofeating2.is_valid():

                formset_specificingredient2.save()
                form_fulldayofeating2.save()

                return redirect(
                    'update-fulldayofeating2',
                    id_fulldayofeating2=fulldayofeating2_object.id
                    )

            else:
                context = {}
                return render(
                    request,
                    'measuredfood/error/form_fulldayofeating_not_valid.html',
                    context)
        else:
            form_fulldayofeating2 = FullDayOfEating2Form(
                request.user.id,
                instance=fulldayofeating2_object
                )
            # Allow the user to only add NutrientProfiles from their own
            # collection.
            form_fulldayofeating2.fields['nutrient_profile'].queryset = \
                NutrientProfile.objects.filter(
                    author=request.user.id
                    )

            formset_specificingredient2 = SpecificIngredient2Formset(
                instance=fulldayofeating2_object
                )

            # Allow the user to only add RawIngredient3s from their own
            # collection.
            for form in formset_specificingredient2:
                form.fields['rawingredient3'].queryset = \
                    RawIngredient3.objects.filter(
                        author=request.user.id
                        )

            context = {
                'formset_specificingredient2': formset_specificingredient2,
                'form_fulldayofeating2': form_fulldayofeating2,
                'id_fulldayofeating2': id_fulldayofeating2,
                }
            return render(request, 'measuredfood/fulldayofeating2_form.html',
                          context)

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


class ListFullDayOfEating2(
    LoginRequiredMixin,
    ListView
):
    model = FullDayOfEating2

    def get_queryset(self):
        return FullDayOfEating2.objects.filter(
            author=self.request.user
        ).order_by('name')


# TODO: Adapt this view to FullDayOfEating2
class DetailFullDayOfEating2(DetailView):
    model = FullDayOfEating2

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Access the FullDayOfEating2 object in order to query the correct
        # specificnutrienttarget_queryset.
        id_full_day_of_eating_ = context['object'].id

        specificingredient_queryset = SpecificIngredient2.objects.filter(
            fulldayofeating=id_full_day_of_eating_
        )
        specificingredient_list = list(
            specificingredient_queryset
        )
        context['specificingredient_list'] = \
            specificingredient_list

        return context


class DeleteFullDayOfEating2(UserPassesTestMixin, DeleteView):
    model = FullDayOfEating2
    success_url = reverse_lazy('list-fulldayofeating2')

    def test_func(self):
        fulldayofeating_ = self.get_object()
        if self.request.user == fulldayofeating_.author:
            return True
        return False


@login_required
def calculate_fulldayofeating2_view(request, id_fulldayofeating2):

    try:

        # Make sure users can not edit other user's objects.
        check_if_author(
            request,
            FullDayOfEating2,
            id_fulldayofeating2,
            UserIsNotAuthorError,
        )

        fulldayofeating2_object = FullDayOfEating2.objects.get(
            pk=id_fulldayofeating2
        )

        specificingredient2_dict_list, \
            nutrientprofile_dict \
            = query_input_and_calculate_fulldayofeating2(
                id_fulldayofeating2,
                SpecificIngredient2,
                query_ingredients_fulldayofeating2,
                pprint,
                RawIngredient3,
                ALL_NUTRIENTS_AND_DEFAULT_UNITS,
                set_to_zero_if_none,
                FullDayOfEating2,
                NutrientProfile,
                query_nutrientprofile_of_fulldayofeating2,
                calculate_fulldayofeating2,
                calculate_average_of_specificingredient2_group,
                copy,
                make_list_variable_ingredient_and_group,
                calculate_specificingredient2_amount_try,
                np,
                NumberTargetedNutrientsNotEqualNumberScalingEntitiesError,
                undo_calculate_average_of_specificingredient2_group,
                make_specificingredient2_id_and_calculated_amount_dict,
                save_fulldayofeating2_calculation_result_to_database,
                logging,
                NoValueForTargetedNutrientError,
            )

        result_calculate_fulldayofeating2_formatted_for_template = \
            prepare_calculation_result_for_display(
                specificingredient2_dict_list,
            )

        aggregated_total_nutrition_not_all_nutrients_displayed = \
            make_aggregated_total_nutrition(
                specificingredient2_dict_list,
                calculate_total_nutrition_fulldayofeating2,
                ALL_NUTRIENTS_AND_DEFAULT_UNITS,
                set_to_zero_if_none,
                calculate_percentage_of_target_amount,
                nutrientprofile_dict,
                calculate_percent_max_fulldayofeating,
                judge_total_nutrition,
                copy,
            )

        context = {
            'id_fulldayofeating2': id_fulldayofeating2,
            'fulldayofeating2_object': fulldayofeating2_object,
            'result_calculate_fulldayofeating_formatted_for_template':
                result_calculate_fulldayofeating2_formatted_for_template,
            'aggregated_total_nutrition_fulldayofeating':
                aggregated_total_nutrition_not_all_nutrients_displayed,
        }

        return render(
            request,
            'measuredfood/fulldayofeating2_calculation_result.html',
            context
        )

    except NoValueForTargetedNutrientError as e:
        list_ = e.nutrient_value_missing
        seperator = ', '
        pretty_list = seperator.join(list_)
        error_message = \
            'The values for the following nutrients in the nutrient profile ' \
            'are missing: '\
            + pretty_list\
            + '.'\
            + ' Please add values for these nutrients in the ' \
              'nutrient profile or do not target them.'
        context = {
            'error_message': error_message,
            'error_id': 'NoValueForTargetedNutrientError',
        }
        return render(
            request,
            'measuredfood/error/general_error_page.html',
            context
        )


# TODO: Adapt this view to FullDayOfEating2
def copy_fulldayofeating2_to_user(request, id_fulldayofeating2):
    """
    From the publicly available full days of eating, copy a full day of
    eating to the user's full day of eating objects.
    :return:
    """

    # Copy the nutrient profile:
    nutrient_profile = FullDayOfEating2.objects.get(
        id=id_fulldayofeating2
    ).nutrient_profile
    nutrient_profile_copy = NutrientProfile.objects.get(
        id=nutrient_profile.id
    )
    nutrient_profile_copy.pk = None
    nutrient_profile_copy.author = request.user
    nutrient_profile_copy.save()

    # Copy the full day of eating, along with the
    # the SpecificIngredient2 and the RawIngredient3 objects.
    full_day_of_eating_copy = FullDayOfEating2.objects.get(
        id=id_fulldayofeating2
    )
    full_day_of_eating_copy.pk = None
    full_day_of_eating_copy.author = request.user
    full_day_of_eating_copy.nutrient_profile = nutrient_profile_copy
    full_day_of_eating_copy.save()

    # Copy all SpecificIngredient2 objects.
    specific_ingredient_queryset = SpecificIngredient2.objects.filter(
        fulldayofeating=id_fulldayofeating2
    )

    for specific_ingredient_k in specific_ingredient_queryset:
        raw_ingredient3_copy = specific_ingredient_k.rawingredient3
        raw_ingredient3_copy.pk = None
        raw_ingredient3_copy.author = request.user
        raw_ingredient3_copy.save()
        specific_ingredient_copy = specific_ingredient_k
        specific_ingredient_copy.pk = None
        specific_ingredient_copy.rawingredient3 = raw_ingredient3_copy
        specific_ingredient_copy.fulldayofeating = full_day_of_eating_copy
        specific_ingredient_copy.save()

    fulldayofeating_list = FullDayOfEating2.objects.filter(
        author=request.user
    ).order_by('name')

    context = {'fulldayofeating_list': fulldayofeating_list}

    return render(
        request,
        'measuredfood/fulldayofeating_list.html',
        context
    )
