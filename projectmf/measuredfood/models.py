from django.db import models

# Create your models here.

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class RawIngredient(models.Model):
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
    
