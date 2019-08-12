from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_NUMBERS,
    INGREDIENT_FIELDS_LINKS,
    INGREDIENT_FIELDS_NUTRITION
)

from string import ascii_lowercase
from .rawingredient import RawIngredient
from .nutrientprofile import NutrientProfile
from .fulldayofeating import FullDayOfEating

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class Mealplan(models.Model):
    """
    Putting many SpecificFullDayOfEating instances together creates a mealplan.
    """

    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-mealplan')
