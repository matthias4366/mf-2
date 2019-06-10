from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    calories = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_
    )
    fat = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_
    )
    protein = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_
    )
    carbohydrates = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # TODO: remove intermediary solution.
        # Now, after creating a raw ingredient, the user is redirected to the
        # home page. They should be redirected to the list of ingredients.
        return reverse('home')
