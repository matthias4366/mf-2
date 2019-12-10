from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from measuredfood.utils.rawingredient3\
    .transform_ingredient_name_usda_to_measuredfood \
    import transform_ingredient_name_usda_to_measuredfood


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

    @staticmethod
    def get_absolute_url():
        return reverse('list-nutrient-profiles')

    class Meta:
        ordering = ["name"]


# Add all the fields related to nutrition to the nutrient profile model.
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:

    # Create a nutrient name for the measured food database based on the
    # nutrient name from the USDA API.
    nutrient_name_measuredfood = \
        transform_ingredient_name_usda_to_measuredfood(
            nutrient_dict['nutrient_name_usda_api'],
            nutrient_dict['id_nutrient_usda_api'],
        )

    # Add the nutrient fields.
    NutrientProfile.add_to_class(
        nutrient_name_measuredfood,
        models.FloatField(
            blank=True,
            null=True
        )
    )
    # Add the nutrient unit fields.
    NutrientProfile.add_to_class(
        nutrient_name_measuredfood+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['unit_nutrient_usda_api'],
                      nutrient_dict['unit_nutrient_usda_api']), ],
            blank=False,
            null=False,
            default=nutrient_dict['unit_nutrient_usda_api'],
        )
    )

    # Add all the fields related to tolerable upper intakes of each
    # nutrient to the nutrient profile model.
    # 'Max' is used to indicate 'maximum' because that is clearer than
    # 'tui' for
    # tolerable upper intake.

    # Add the nutrient fields.
    NutrientProfile.add_to_class(
        'max_'+nutrient_name_measuredfood,
        models.FloatField(
            blank=True,
            null=True
        )
    )
    # Add the nutrient unit fields.
    NutrientProfile.add_to_class(
        'max_'+nutrient_name_measuredfood+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['unit_nutrient_usda_api'],
                      nutrient_dict['unit_nutrient_usda_api']), ],
            blank=False,
            null=False,
            default=nutrient_dict['unit_nutrient_usda_api'],
        )
    )
