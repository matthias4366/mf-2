from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.utils.rawingredient3.\
    transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood

from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
    INGREDIENT_FIELDS_LINKS,
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

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount = models.FloatField(
        blank=True,
        null=False,
        default=100,
        editable=False,
    )

    # In the USDA database, the 'Carbohydrate, by difference' value includes
    # the fibre. Of course, the number of carbohydrates should not include
    # fiber. The number of carbohydrate_without_fiber is calculated by
    # subtracting the number of 'Carbohydrate, by difference' and
    # 'Fiber, total dietary'.
    carbohydrate_without_fiber = models.FloatField(
        blank=True,
        null=True,
        # The verbose_name is used to set the field labels on the
        # RawIngredient3Form.
        verbose_name='Carbohydrate without fiber',
    )
    carbohydrate_without_fiber_unit = models.CharField(
        max_length=100,
        choices=[('g',
                  'g'), ],
        blank=False,
        null=False,
        default='g',
        verbose_name='Carbohydrate without fiber unit',
    )

    class Meta:
        ordering = ["name"]
        # So the user does not get confused, they must give unique names to
        # their RawIngredient3 objects. Different users can use the same names.
        unique_together = (
            ("name", "author"),
        )

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('list-raw-ingredient-usda')


for name in INGREDIENT_FIELDS_LINKS:
    RawIngredient3.add_to_class(
        name,
        models.URLField(
            max_length=1000,
            blank=True,
            null=True)
    )


# Nutrients
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # Create a nutrient name for the measured food database based on the
    # nutrient name from the USDA API.
    nutrient_name_measuredfood = \
        transform_nutrient_name_usda_to_measuredfood(
            nutrient_dict['nutrient_name_usda_api'],
            nutrient_dict['id_nutrient_usda_api']
        )

    # add the nutrient fields
    RawIngredient3.add_to_class(
        nutrient_name_measuredfood,
        models.FloatField(
            blank=True,
            null=True,
            # The verbose_name is used to set the field labels on the
            # RawIngredient3Form.
            verbose_name=nutrient_dict['nutrient_name_usda_api'],
        )
    )
    # add the nutrient unit fields.
    RawIngredient3.add_to_class(
        nutrient_name_measuredfood+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['unit_nutrient_usda_api'],
                      nutrient_dict['unit_nutrient_usda_api']), ],
            blank=False,
            null=False,
            default=nutrient_dict['unit_nutrient_usda_api'],
            verbose_name=nutrient_dict['nutrient_name_usda_api']+' unit',
        )
    )
