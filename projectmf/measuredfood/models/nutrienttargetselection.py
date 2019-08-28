from django.db import models
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)


class NutrientTargetSelection(models.Model):
    """
    The total of the daily nutrient goals is stored in the NutrientProfile.
    However, when calculating the ingredient amounts in the FullDayOfEating,
    that calculation is based on only the nutrients selected in the
    NutrientTargetSelection.

    TODO: delete this once the newer, better model is ready.

    """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# add all the fields related to nutrition to the nutrient profile model
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    field_name = nutrient_dict['name'] + '_is_targeted'
    # add the nutrient fields
    NutrientTargetSelection.add_to_class(
        field_name,
        models.BooleanField(
            blank=False,
            null=False,
            default=False,
        )
    )
