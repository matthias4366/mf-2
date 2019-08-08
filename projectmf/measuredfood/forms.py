from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from measuredfood.models import (
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile,
    RawIngredient,
    Mealplan
    )
from django.forms import inlineformset_factory
import pprint

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class SpecificIngredientForm(forms.ModelForm):
#     """This class does not currently do anything."""
#
#     class Meta:
#         model = SpecificIngredient
#         fields = '__all__'
#         exclude = ['author']


class FullDayOfEatingForm(forms.ModelForm):

    class Meta:
        model = FullDayOfEating
        fields = '__all__'
        exclude = ['author']

    # Prevent the users from using the NutrientProfiles of other users when
    # creating a full day of eating.
    def __init__(self, id_user, *args, **kwargs):
        super(FullDayOfEatingForm, self).__init__(*args, **kwargs)
        self.fields['nutrient_profile'].queryset = \
        NutrientProfile.objects.filter(author_id=id_user)


class NutrientProfileForm(forms.ModelForm):

    class Meta:
        model = NutrientProfile
        fields = '__all__'
        exclude = ['author']


SpecificIngredientFormset = inlineformset_factory(
    FullDayOfEating,
    SpecificIngredient,
    fields=('__all__'),
    extra=1,
    )


class MealplanForm(forms.ModelForm):

    class Meta:
        model = Mealplan
        exclude = ['author']

    # TODO: Important error. Only query the FullDayOfEating objects that belong
    # to the user.
    fulldayofeating = forms.ModelMultipleChoiceField(
        queryset = FullDayOfEating.objects.all()
    )
