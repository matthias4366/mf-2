from django.db import models
from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from .fulldayofeating import FullDayOfEating

from measuredfood.utils.rawingredient3\
    .transform_ingredient_name_usda_to_measuredfood \
    import transform_ingredient_name_usda_to_measuredfood

choices_nutrient_names = []
# For the choice field, create a tuple with the nutrients.
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # Do not display a part of the nutrients defined in the nutrients.csv
    # file. The reason is to not overwhelm the user.
    if not nutrient_dict['display_in_ingredient_form']:
        continue
    # Create a nutrient name for the measured food database based on the
    # nutrient name from the USDA API.
    nutrient_name_measuredfood = \
        transform_ingredient_name_usda_to_measuredfood(
            nutrient_dict['nutrient_name_usda_api'],
            nutrient_dict['id_nutrient_usda_api'],
        )
    nutrient_name = nutrient_name_measuredfood
    # The second element of the tuple is the human readable name.
    # Therefore, the nutrient_name_usda_api will be inserted here.
    new_tuple = (nutrient_name, nutrient_dict['nutrient_name_usda_api'])
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
