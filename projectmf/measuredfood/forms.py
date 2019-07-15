from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from measuredfood.models import SpecificIngredient

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SpecificIngredientForm(forms.ModelForm):

    class Meta:
        model = SpecificIngredient
        fields = '__all__'
        exclude = ['author']
