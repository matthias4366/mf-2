from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .ingredient_properties import (
    INGREDIENT_FIELDS_NUMBERS,
    INGREDIENT_FIELDS_LINKS,
    INGREDIENT_FIELDS_NUTRITION
)

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6

from string import ascii_lowercase


class RawIngredient(models.Model):
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-raw-ingredients')


for name in INGREDIENT_FIELDS_NUMBERS:
    RawIngredient.add_to_class(
        name,
        models.DecimalField(
            max_digits=MAX_DIGITS_,
            decimal_places=DECIMAL_PLACES_,
            blank=True,
            null=True
        )
    )

for name in INGREDIENT_FIELDS_LINKS:
    RawIngredient.add_to_class(
        name,
        models.URLField(
        max_length=1000,
        blank=True,
        null=True)
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

    def get_absolute_url(self):
        return reverse('list-nutrient-profiles')

# add all the fields related to nutrition to the nutrient profile model
for name in INGREDIENT_FIELDS_NUTRITION:
    NutrientProfile.add_to_class(
        name,
        models.DecimalField(
            max_digits=MAX_DIGITS_,
            decimal_places=DECIMAL_PLACES_,
            blank=True,
            null=True
        )
    )


class Mealplan(models.Model):
    """
    Putting many FullDayOfEating instances together creates a mealplan.
    TODO: write the code for this class.
    """

    name = models.CharField(max_length=100)


class FullDayOfEating(models.Model):
    """
    Putting many recipes and single ingredients together creates a full day of
    eating.
    TODO: write the code for this class and create the correct relationships.
    """

    name = models.CharField(max_length=100)


class Recipe(models.Model):

    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-recipes')


class SpecificIngredient(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    rawingredient = models.ForeignKey(
        RawIngredient,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    """
    The base amounts give starting values for the amounts for the ingrediens.
    If the group_or_fixed value is set to fixed, the amount already represents
    the final amount. Furthermore, if two ingredients have the same
    fixed_or_group group assignement, they will stay in the same ratio to each
    other. So, the base_amounts are important for the ratios of the ingredients
    at a later point.
    """
    base_amount = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True
    )

    # Units
    GRAM = 'g'
    MILLILITRE = 'ml'
    PILL = 'pill'

    BASE_AMOUNT_UNIT_CHOICES = [
        (GRAM, 'gram'),
        (MILLILITRE, 'milli litre'),
        (PILL, 'pill'),
    ]

    base_amount_unit = models.CharField(
        max_length = 100,
        choices = BASE_AMOUNT_UNIT_CHOICES,
        default = GRAM,
    )

    # Group or fixed
    GROUP_OR_FIXED_CHOICES = [
        ('FIXED', 'fixed'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
        ('M', 'M'),
        ('N', 'N'),
        ('O', 'O'),
        ('P', 'P'),
        ('Q', 'Q'),
        ('R', 'R'),
        ('S', 'S'),
        ('T', 'T'),
        ('U', 'U'),
        ('V', 'V'),
        ('W', 'W'),
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z'),
    ]

    group_or_fixed = models.CharField(
        max_length = 100,
        choices = GROUP_OR_FIXED_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        label = self.rawingredient.name + ' for ' + self.recipe.name
        return label
