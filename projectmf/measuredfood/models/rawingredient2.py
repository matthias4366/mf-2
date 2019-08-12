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


class RawIngredient2(models.Model):
    """
    Revision of RawIngredient. Once the app has fully moved to RawIngredient2,
    RawIngredient can be deleted. Renaming is not absolutely necessary,
    as this might not be the only revision.
    """
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
    price_per_reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 0
    )
    # TODO: code this as a choice field.
    # Start with the choices "EURO" and "DOLLAR".
    # currency_price_per_reference_amount

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 100
    )
    # TODO: code this as a choice field.
    # Have gram as the only choice for now.
    # reference_amount_unit

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-rawingredient2')
