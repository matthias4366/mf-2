from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .ingredient_properties import (
    INGREDIENT_FIELDS_NUMBERS,
    INGREDIENT_FIELDS_LINKS,
    INGREDIENT_FIELDS_NUTRITION
)

from string import ascii_lowercase

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6

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

    # Price of the ingredient per reference amount
    price_eur_per_reference_amount = models.FloatField(
        blank = False,
        null = False,
        default = 0
    )

    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    reference_amount_g = models.FloatField(
        blank = False,
        null = False,
        default = 100
    )



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-raw-ingredients')


for name in INGREDIENT_FIELDS_NUMBERS:
    RawIngredient.add_to_class(
        name,
        models.FloatField(
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
        models.FloatField(
            blank=True,
            null=True
        )
    )

# For each nutrient, add a field with the information about whether that
# nutrient is targeted when the tailored ingredient amounts are calculated.
for name in INGREDIENT_FIELDS_NUTRITION:
    name_field = name + '_is_targeted'
    NutrientProfile.add_to_class(
        name_field,
        models.BooleanField(
            default = False
        )
    )


class FullDayOfEating(models.Model):
    """
    Putting many recipes and single ingredients together creates a full day of
    eating.
    TODO: write the code for this class and create the correct relationships.
    """

    name = models.CharField(max_length=100)

    notes = models.TextField(null=True, blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )

    # Every full day of eating is linked with one nutrient_profile.
    # But one nutrient_profile can be linked to many full days of eating.
    nutrient_profile = models.ForeignKey(
        NutrientProfile,
        # TODO: I am not sure about the on_delete option.
        on_delete=models.SET_NULL,
        editable = True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('list-recipes')


class Mealplan(models.Model):
    """
    Putting many FullDayOfEating instances together creates a mealplan.
    """

    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    fulldayofeating = models.ManyToManyField(
        FullDayOfEating
    )


class Recipe(models.Model):

    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable = False
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-recipes')


class SpecificIngredient(models.Model):
    # This class does not need an author, as it is linked to a specific
    # FullDayOfEating and the FullDayOfEating has an author.

    # A specific ingredient can't both belong to a recipe AND to a
    # FullDayOfEating. This is complicated, so I will forget about
    # the recipes for now.
    fulldayofeating = models.ForeignKey(
        FullDayOfEating,
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    rawingredient = models.ForeignKey(
        RawIngredient,
        on_delete=models.CASCADE,
        blank=False,
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
    # base_amount = models.FloatField(
    #     blank=False,
    #     null=True
    # )
    base_amount = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=False,
        null=True
    )

    calculated_amount = models.FloatField(
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

    """
    The scaling option defines option that are applied in the scaling of
    the amount of an ingredient. Some ingredients should not be scaled,
    i.e. the amount should be fixed. Some ingredients should be scaled
    independently of the other ingredients. Some ingredients should be scaled
    in relation to other ingredients, in order to maintain the taste of the
    recipe in the scaling process. For example there could be a set relationship
    between chili powder and rice. This would be implemented by assigning both
    the chili powder and the rice to group A.
    """
    SCALING_OPTION_CHOICES = [
        ('FIXED', 'fixed'),
        ('INDEPENDENT', 'independent'),
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

    scaling_option = models.CharField(
        max_length = 100,
        choices = SCALING_OPTION_CHOICES,
        # blank=True,
        # null=True,
        default = 'FIXED'
    )

    def __str__(self):
        if self.rawingredient.name is not None:
            label = self.rawingredient.name
            return label
        else:
            return 'SpecificIngredient without an associated RawIngredient'
