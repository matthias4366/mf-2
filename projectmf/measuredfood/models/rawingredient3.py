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
    price_per_reference_amount = models.FloatField(
        blank=True,
        null=True,
        default=0
    )

    currency_of_price_per_reference_amount = models.CharField(
        max_length=100,
        choices=[('euro', 'euro'), ],
        blank=False,
        null=False,
        default='euro',
    )

    # Amount in package to round up shopping list.
    amount_in_package = models.FloatField(
            blank=True,
            null=True,
        )
    amount_in_package_unit = models.CharField(
        max_length=100,
        choices=[('gram', 'gram'), ],
        blank=False,
        null=False,
        default='gram',
    )

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount = models.FloatField(
        blank=True,
        null=False,
        default=100
    )

    reference_amount_unit = models.CharField(
        max_length=100,
        choices=[('gram', 'gram'), ],
        blank=False,
        null=False,
        default='gram',
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
    # Ignore the nutrient names from the USDA database that are actually
    # section titles, such as "Vitamins" and "Minerals".
    if nutrient_dict['nutrient_name_measuredfood'] is not 'ignore':
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
