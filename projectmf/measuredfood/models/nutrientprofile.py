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

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class NutrientProfile(models.Model):
    """
    This model holds the target values for all the nutrients.
    The target values are to be by calculating the correct ingredient amounts.
    """
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-nutrient-profiles')

# add all the fields related to nutrition to the nutrient profile model
for name in INGREDIENT_FIELDS_NUTRITION:
    NutrientProfile.add_to_class(
        name,
        models.FloatField(
            blank=True,
            null=True
        )
    )

# For each nutrient, add a field with the information about whether that
# nutrient is targeted when the tailored ingredient amounts are calculated.
for name in INGREDIENT_FIELDS_NUTRITION:
    name_field = name + '_is_targeted'
    NutrientProfile.add_to_class(
        name_field,
        models.BooleanField(
            default = False
        )
    )
