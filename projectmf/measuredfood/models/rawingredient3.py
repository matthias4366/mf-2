from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from measuredfood.utils.rawingredient3.\
    transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood

from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
    INGREDIENT_FIELDS_LINKS,
)
from measuredfood.utils.make_displayed_name import make_displayed_name
import copy

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
    # Actually, the reference amount has to be editable because of the
    # vitamin tablets, as they have a reference amount of 1g.
    reference_amount = models.FloatField(
        blank=True,
        null=False,
        default=100,
    )

    # # FoodData Central id - the unique id used to identify a food in the
    # # FoodData Central database. This id is saved to the RawIngredient3 model
    # # when an ingredient is retrieved from the FoodData Central API and saved
    # # as a RawIngredient3 model.
    # fdcid = models.FloatField(
    #     blank=True,
    #     null=False,
    #     editable=False,
    # )

    class Meta:
        ordering = ["name"]

    def get_full_name(self):
        displayed_name = make_displayed_name(
            self.name,
            self.id
        )
        return displayed_name

    def __str__(self):
        max_name_length = 15
        shortened_name = copy.deepcopy(self.name)
        if len(self.name) > max_name_length:
            shortened_name = shortened_name[0:max_name_length] + '...'
        displayed_name = make_displayed_name(
            shortened_name,
            self.id
        )
        return displayed_name

    @staticmethod
    def get_absolute_url():
        return reverse('list-raw-ingredient-usda')

    def get_detail_view_url(self):
        return "/rawingredient3/%i/detail/" % self.id


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
