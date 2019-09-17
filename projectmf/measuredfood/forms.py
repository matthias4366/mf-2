from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from measuredfood.models import (
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile,
    RawIngredient2,
    Mealplan,
    SpecificFullDayOfEating,
    SpecificNutrientTarget,
    )

from django.forms import inlineformset_factory


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


class NutrientProfileForm(forms.ModelForm):

    class Meta:
        model = NutrientProfile
        fields = '__all__'
        exclude = ['author']


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


class RawIngredient2Form(forms.ModelForm):

    class Meta:
        model = RawIngredient2
        fields = '__all__'
        exclude = ['author']


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
