from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties import (
    INGREDIENT_FIELDS_NUMBERS,
    INGREDIENT_FIELDS_LINKS,
    INGREDIENT_FIELDS_NUTRITION
)

from string import ascii_lowercase
from .rawingredient import RawIngredient
from .nutrientprofile import NutrientProfile
from .fulldayofeating import FullDayOfEating

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class SpecificIngredient(models.Model):

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
