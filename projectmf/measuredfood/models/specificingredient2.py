from django.db import models
from .rawingredient3 import RawIngredient3
from .fulldayofeating2 import FullDayOfEating2

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6

from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from measuredfood.utils.rawingredient3\
    .transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood

choices_nutrient_names = []
# For the choice field, create a tuple with the nutrients.
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
    # Do not display a part of the nutrients defined in the nutrients.csv
    # file. The reason is to not overwhelm the user.
    if not nutrient_dict['is_displayed']:
        continue
    # Create a nutrient name for the measured food database based on the
    # nutrient name from the USDA API.
    nutrient_name_measuredfood = \
        transform_nutrient_name_usda_to_measuredfood(
            nutrient_dict['nutrient_name_usda_api'],
            nutrient_dict['id_nutrient_usda_api'],
        )
    nutrient_name = nutrient_name_measuredfood
    # The second element of the tuple is the human readable name.
    # Therefore, the nutrient_name_usda_api will be inserted here.
    new_tuple = (nutrient_name, nutrient_dict['nutrient_name_usda_api'])
    choices_nutrient_names.append(new_tuple)


class SpecificIngredient2(models.Model):
    """
    SpecificIngredient2 contains the additional options necessary to use the
    calculate_ingredient_amount_slsqp function. This function will give the
    user more powerful tools to calculate a full day of eating (called
    FullDayOfEating2).
    """

    fulldayofeating2 = models.ForeignKey(
        FullDayOfEating2,
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    rawingredient3 = models.ForeignKey(
        RawIngredient3,
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
        null=False,
        default=100,
    )

    calculated_amount = models.FloatField(
        blank=True,
        null=True
    )

    """
    The min_amount allows the user to define a minimum amount of an 
    ingredient. Let's say the user wants to use a minimum of 30 g of 
    flaxseeds in order to make sure they are getting their essential fatty 
    acids, even if that actually puts them over their daily fat target.
    """
    min_amount = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True,
    )

    """
    The max_amount allows the user to define a maximum amount of an 
    ingredient. Let's say, they are making carbonara and regardless of the 
    protein and fat requirements, they do not want to use more than 200 g of 
    bacon because it is expensive and their pan is not that big.
    """
    max_amount = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True,
    )

    """
    Some ingredients are adjusted in steps. For example, no one wants to get 
    a recipe that calls for 1.18 eggs. The amount of eggs should be adapted 
    in steps of one whole egg.
    """
    step_size = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True,
    )

    """
    An exact value has been calculated (e.g. 146 g) and it lies between two 
    steps (e.g. 120 g and 160 g). It's possible to either pick the closest 
    value, always pick the lower value or always pick the higher value.
    """
    ROUND_STEP_CHOICES = [
        ('round down', 'round down'),
        ('closest value', 'closest value'),
        ('round up', 'round up'),
    ]

    round_step = models.CharField(
        max_length=100,
        choices=ROUND_STEP_CHOICES,
        default='closest value'
    )

    """
    SpecificIngredient2 objects are to be set up with a targeted nutrient in 
    mind. For example, rice is used to reach the carbohydrate target and 
    protein powder is used to reach the protein target. 
    
    During calculation, some SpecificIngredient amounts might be set and then 
    the calculation is redone without that SpecificIngredient. For the 
    calculation to still work, a nutrient target must be removed as well.
    """
    nutrient_target = models.CharField(
        choices=choices_nutrient_names,
        max_length=100,
        blank=True,
        null=True
    )
    """
    Throughout the calculation, the ingredient amount can be varied. If it 
    is false, the ingredient amount stays fixed.
    """

    amount_is_variable = models.BooleanField(
        default=False,
    )

    GROUP_CHOICES = [
        ('no group', 'no group'),
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

    group = models.CharField(
        max_length=100,
        choices=GROUP_CHOICES,
        # blank=True,
        # null=True,
        default='no group'
    )

    def __str__(self):
        if self.rawingredient3.name is not None:
            label = self.rawingredient3.name
            return label
        else:
            return 'SpecificIngredient without an associated RawIngredient'
