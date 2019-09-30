from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
    INGREDIENT_FIELDS_LINKS
)


# The unit choices have been implemented for extensibility, so it is easier
# to add more unit choices later. Currently, the user de facto has no choice.


class RawIngredient2(models.Model):
    """
    Revision of RawIngredient. Once the app has fully moved to RawIngredient2,
    RawIngredient can be deleted. Renaming is not absolutely necessary,
    as this might not be the only revision.
    """
    """
    10.6.2019. The RawIngredient model represents the raw ingredients.
    The user adds the ingredients themselves. They can't pull ingredients from
    a database or share ingredients with other users (yet). These ingredients
    serve as the basis for creating recipes.
    """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True)

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

    """
    The plan is to have a common pool of pre existing RawIngredient2 objects
    from which the user can pull RawIngredient2 objects.
    The is_public property defines whether a RawIngredient2 object is
    part of that pool.
    There are two reasons for this:
    1) The user might be concerned about their privacy and not want their
    RawIngredient2 object be a part of the common pool.
    2) More importantly: the RawIngredient2 objects in the common pool should
    be of high quality, i.e. correct. Users should put thought into a
    RawIngredient2 object before publishing it.
    """
    is_public = models.BooleanField(
        default=False,
        null=False,
    )

    """
    imported_from is currently a placeholder. When searching through the 
    ingredients in the common database, the source of the ingredient is of 
    interest. If it was added by a user, it might not be correct. If it was
    added by Matthias manually, it is more likely to be correct, but could 
    still be wrong. If it was added through automated import from a separate, 
    reputable database, it is most likely correct.   
    """
    imported_from = models.CharField(
        max_length=100,
        choices=[
            ('manually created by user', 'manually created by user'),
            ('manually created by matthias', 'manually created by matthias'),
            ('automatically imported from database xyz', 'automatically '
                                                         'imported from '
                                                         'database xyz'),
        ],
        # The blank and null settings were set to be uncomplicated while
        # the rest of the code is being developed.
        blank=True,
        null=True,
        default='manually created by user',
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('list-rawingredient2')


# Nutrients
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # add the nutrient fields
    RawIngredient2.add_to_class(
        nutrient_dict['name'],
        models.FloatField(
            blank=True,
            null=True,
        )
    )
    # add the nutrient unit fields.
    RawIngredient2.add_to_class(
        nutrient_dict['name']+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['default_unit'],
                      nutrient_dict['default_unit']), ],
            blank=False,
            null=False,
            default=nutrient_dict['default_unit'],
        )
    )

for name in INGREDIENT_FIELDS_LINKS:
    RawIngredient2.add_to_class(
        name,
        models.URLField(
            max_length=1000,
            blank=True,
            null=True)
    )
