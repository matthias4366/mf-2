from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_NUMBERS,
    INGREDIENT_FIELDS_LINKS,
    INGREDIENT_FIELDS_NUTRITION
)

from string import ascii_lowercase

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class RawIngredient(models.Model):
    """
    10.6.2019. The RawIngredient model represents the raw ingredients.
    The user adds the ingredients themselves. They can't pull ingredients from
    a database or share ingredients with other users (yet). These ingredients
    serve as the basis for creating recipes.
    """
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Price of the ingredient per reference amount
    price_eur_per_reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 0
    )

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount_g = models.FloatField(
        blank = False,
        null = False,
        default = 100
    )



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-raw-ingredients')


for name in INGREDIENT_FIELDS_NUMBERS:
    RawIngredient.add_to_class(
        name,
        models.FloatField(
            blank=True,
            null=True
        )
    )

for name in INGREDIENT_FIELDS_LINKS:
    RawIngredient.add_to_class(
        name,
        models.URLField(
        max_length=1000,
        blank=True,
        null=True)
    )
