from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from string import ascii_lowercase
from .nutrientprofile import NutrientProfile
from .fulldayofeating import FullDayOfEating
from .mealplan import Mealplan

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class SpecificFullDayOfEating(models.Model):
    """
    The principle here is the same as with RawIngredient and SpecificIngredient.
    Here is is FullDayOfEating and SpecificFullDayOfEating.
    SpecificFullDayOfEating is used to composite a Mealplan.
    Each SpecificFullDayOfEating has an associated Mealplan and an associated
    FullDayOfEating and serves as the glue between the two.
    """

    fulldayofeating = models.ForeignKey(
        FullDayOfEating,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    mealplan = models.ForeignKey(
        Mealplan,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
