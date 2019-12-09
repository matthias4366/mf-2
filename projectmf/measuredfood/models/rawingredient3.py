from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from measuredfood.ingredient_properties3 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
)

# The unit choices have been implemented for extensibility, so it is easier
# to add more unit choices later. Currently, the user de facto has no choice.


class RawIngredient3(models.Model):
    """
    Revision of RawIngredient2 so that ingredients from the FoodData Central
    database can be imported into measuredfood.
    """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Price of the ingredient per reference amount
    price_per_100_gram = models.FloatField(
        blank=True,
        null=True,
        default=0
    )

    currency_of_price_per_100_gram = models.CharField(
        max_length=100,
        choices=[('\u20ac', '\u20ac'), ],
        blank=False,
        null=False,
        default='\u20ac',
    )

    # Amount in package to round up shopping list.
    amount_in_package = models.FloatField(
            blank=True,
            null=True,
        )
    amount_in_package_unit = models.CharField(
        max_length=100,
        choices=[('g', 'g'), ],
        blank=False,
        null=False,
        default='g',
    )

    class Meta:
        ordering = ["name"]
        # So the user does not get confused, they must give unique names to
        # their RawIngredient2 objects. Different users can use the same names.
        unique_together = (
            ("name", "author"),
        )

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('list-raw-ingredient-usda')


# Nutrients
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # Ignore incomplete nutrient_dict.
    if len(nutrient_dict['id_nutrient_usda_api']) > 0 and \
            len(nutrient_dict['nutrient_name_measuredfood']) > 0:
        # add the nutrient fields
        RawIngredient3.add_to_class(
            nutrient_dict['nutrient_name_measuredfood'],
            models.FloatField(
                blank=True,
                null=True,
            )
        )
        # add the nutrient unit fields.
        RawIngredient3.add_to_class(
            nutrient_dict['nutrient_name_measuredfood']+'_unit',
            models.CharField(
                max_length=100,
                choices=[(nutrient_dict['unit_nutrient_usda_api'],
                          nutrient_dict['unit_nutrient_usda_api']), ],
                blank=False,
                null=False,
                default=nutrient_dict['unit_nutrient_usda_api'],
            )
        )
