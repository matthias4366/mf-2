from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)


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


# add all the fields related to nutrition to the nutrient profile model
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # add the nutrient fields
    NutrientProfile.add_to_class(
        nutrient_dict['name'],
        models.FloatField(
            blank=True,
            null=True
        )
    )
    # add the nutrient unit fields.
    NutrientProfile.add_to_class(
        nutrient_dict['name']+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['default_unit'], nutrient_dict['default_unit']), ],
            blank=False,
            null=False,
            default=nutrient_dict['default_unit'],
        )
    )
