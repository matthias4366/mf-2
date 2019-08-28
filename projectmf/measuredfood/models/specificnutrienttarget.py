from django.db import models
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from .fulldayofeating import FullDayOfEating

choices_nutrient_names = []
# For the choice field, create a tuple with the nutrients.
for nutrient_dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    nutrient_name = nutrient_dict_k['name']
    new_tuple = (nutrient_name, nutrient_name)
    choices_nutrient_names.append(new_tuple)


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
        choices=choices_nutrient_names,
        max_length=100,
        blank=False,
        null=True
        )

    def __str__(self):
        if self.nutrient_target is not None:
            label = self.nutrient_target
            return label
        else:
            return 'SpecificNutrientTarget without a NutrientTarget'
