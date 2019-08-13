from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    VITAMINS_AND_DEFAULT_UNITS,
    ELEMENTS_AND_DEFAULT_UNITS,
)

from string import ascii_lowercase

# The unit choices have been implemented for extensibility, so it is easier
# to add more unit choices later.
MASS_UNIT_CHOICES = [
    ('gram', 'gram'),
    ('milligram', 'milligram'),
    ('microgram', 'microgram'),
]
MASS_UNIT_DEFAULT_CHOICE = 'gram'

VITAMIN_AND_ELEMENT_UNIT_CHOICES = [
    ('gram', 'gram'),
    ('milligram', 'milligram'),
    ('microgram', 'microgram'),
    ('international units', 'international units')
]

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
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Price of the ingredient per reference amount
    price_per_reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 0
    )

    currency_of_price_per_reference_amount = models.CharField(
        max_length = 100,
        choices = [('euro', 'euro'),],
        blank = False,
        null = False,
        default = 'euro',
    )

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 100
    )

    reference_amount_unit = models.CharField(
        max_length = 100,
        choices = MASS_UNIT_CHOICES,
        blank = False,
        null = False,
        default = MASS_UNIT_DEFAULT_CHOICE,
    )

    # Calories
    calories = models.FloatField(
        blank = False,
        null = True,
    )
    calories_unit = models.CharField(
        max_length = 100,
        choices = [('kcal', 'kcal'),],
        blank = False,
        null = False,
        default = 'kcal',
    )

    # Macronutrients
    # Carbohydrates
    carbohydrates = models.FloatField(
        blank = False,
        null = True,
    )
    carbohydrates_unit = models.CharField(
        max_length = 100,
        choices = [('gram', 'gram'),],
        blank = False,
        null = False,
        default = MASS_UNIT_DEFAULT_CHOICE,
    )

    # Fat
    fat = models.FloatField(
        blank = False,
        null = True,
    )
    fat_unit = models.CharField(
        max_length = 100,
        choices = [('gram', 'gram')],
        blank = False,
        null = False,
        default = 'gram',
    )

    # Protein
    protein = models.FloatField(
        blank = False,
        null = True,
    )
    protein_unit = models.CharField(
        max_length = 100,
        choices = [('gram', 'gram')],
        blank = False,
        null = False,
        default = 'gram',
    )

    # Essential fats
    # Linoleic acid
    linoleic_acid = models.FloatField(
        blank = False,
        null = True,
    )
    linoleic_acid_unit = models.CharField(
        max_length = 100,
        choices = [('gram', 'gram')],
        blank = False,
        null = False,
        default = 'gram',
    )

    # Alpha linoleic acid
    alpha_linoleic_acid = models.FloatField(
        blank = False,
        null = True,
    )
    alpha_linoleic_acid_unit = models.CharField(
        max_length = 100,
        choices = [('gram', 'gram')],
        blank = False,
        null = False,
        default = 'gram',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-rawingredient2')

# Vitamins

for vitamin_dict in VITAMINS_AND_DEFAULT_UNITS:
    # add the vitamin fields
    RawIngredient2.add_to_class(
        vitamin_dict['name'],
        models.FloatField(
            blank=True,
            null=True,
        )
    )
    # add the vitamin unit fields.
    RawIngredient2.add_to_class(
        vitamin_dict['name']+'_unit',
        models.CharField(
            max_length = 100,
            choices = [(vitamin_dict['default_unit'], vitamin_dict['default_unit']),],
            blank = False,
            null = False,
            default = vitamin_dict['default_unit'],
        )
    )

# Elements
for element_dict in ELEMENTS_AND_DEFAULT_UNITS:
    # add the element fields
    RawIngredient2.add_to_class(
        element_dict['name'],
        models.FloatField(
            blank=True,
            null=True,
        )
    )
    # add the element unit fields.
    RawIngredient2.add_to_class(
        element_dict['name']+'_unit',
        models.CharField(
            max_length = 100,
            choices = [(element_dict['default_unit'], element_dict['default_unit']),],
            blank = False,
            null = False,
            default = element_dict['default_unit'],
        )
    )
