from django.db import models
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from .fulldayofeating import FullDayOfEating

class SpecificNutrientTarget(models.Model):
    """
    The nutrient target selection determines which nutrients are used in the
    calculation of the amounts of the ingredients.

    This is a rework of the NutrientTargetSelection model.
    """

    fulldayofeating = models.ForeignKey(
        FullDayOfEating,
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    nutrient_target = models.CharField(
        max_length=100,
        blank=False,
        null=True
        )
