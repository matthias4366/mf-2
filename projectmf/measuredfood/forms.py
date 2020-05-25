from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from measuredfood.models import (
    SpecificIngredient,
    SpecificIngredient2,
    FullDayOfEating,
    FullDayOfEating2,
    NutrientProfile,
    RawIngredient3,
    Mealplan,
    SpecificFullDayOfEating,
    SpecificNutrientTarget,
    InformationForNutrientProfile,
    )
from measuredfood.utils.rawingredient3\
    .transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood

from django.forms import inlineformset_factory
import json

from pathlib import Path

path_to_nutrient_dict_list_json = Path(
    __file__).parent.parent.joinpath('data').joinpath('nutrient_dict_list.json')

with open(path_to_nutrient_dict_list_json, 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

# List of fields to display in NutrientProfileForm.
# Which fields are displayed is stored in nutrient.csv.
# The purpose is to not overwhelm the user with the number of nutrients,
# a lot of which are not important enough to care about.
exclude_ = ['author']
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    if not nutrient_dict['is_displayed']:
        nutrient_name_measuredfood = \
            transform_nutrient_name_usda_to_measuredfood(
                nutrient_dict['nutrient_name_usda_api'],
                nutrient_dict['id_nutrient_usda_api'],
            )
        exclude_.append(
            nutrient_name_measuredfood
        )
        exclude_.append(
            nutrient_name_measuredfood + '_unit'
        )
        # The following fields are part of the nutrient profile form.
        exclude_.append(
            'max_'+nutrient_name_measuredfood
        )
        exclude_.append(
            'max_'+nutrient_name_measuredfood + '_unit'
        )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FullDayOfEatingForm(forms.ModelForm):

    class Meta:
        model = FullDayOfEating
        fields = '__all__'
        exclude = ['author']

    # Prevent the users from using the NutrientProfiles
    # of other users when
    # creating a full day of eating.
    def __init__(self, id_user, *args, **kwargs):
        super(FullDayOfEatingForm, self).__init__(*args, **kwargs)
        self.fields['nutrient_profile'].queryset = \
            NutrientProfile.objects.filter(author_id=id_user)


class FullDayOfEating2Form(forms.ModelForm):

    class Meta:
        model = FullDayOfEating2
        fields = '__all__'
        exclude = ['author']

    # Prevent the users from using the NutrientProfiles
    # of other users when
    # creating a full day of eating.
    def __init__(self, id_user, *args, **kwargs):
        super(FullDayOfEating2Form, self).__init__(*args, **kwargs)
        self.fields['nutrient_profile'].queryset = \
            NutrientProfile.objects.filter(author_id=id_user)


class NutrientProfileForm(forms.ModelForm):

    class Meta:
        model = NutrientProfile
        fields = '__all__'
        exclude = exclude_


SpecificIngredientFormset = inlineformset_factory(
    FullDayOfEating,
    SpecificIngredient,
    fields='__all__',
    extra=1,
    )


class MealplanForm(forms.ModelForm):

    class Meta:
        model = Mealplan
        exclude = ['author']


SpecificFullDayOfEatingFormset = inlineformset_factory(
    Mealplan,
    SpecificFullDayOfEating,
    fields='__all__',
    extra=1,
)


class RawIngredient3Form(forms.ModelForm):

    class Meta:
        model = RawIngredient3
        fields = '__all__'
        exclude = exclude_


class SpecificNutrientTargetForm(forms.ModelForm):

    class Meta:
        model = SpecificNutrientTarget
        fields = '__all__'


SpecificNutrientTargetFormset = inlineformset_factory(
    FullDayOfEating,
    SpecificNutrientTarget,
    fields='__all__',
    extra=1,
    )


class FoodDataCentralIDForm(forms.Form):
    """
    The user can search for an ingredient on FoodData Central, copy the FDC
    ID into the form and the ingredient will be added to the user's ingredients.
    """
    FDC_ID = forms.CharField(
        label='FDC ID',
        max_length=100,
    )


class InformationForNutrientProfileForm(forms.ModelForm):

    class Meta:
        model = InformationForNutrientProfile
        exclude = ['user']
