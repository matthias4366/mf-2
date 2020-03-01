from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from measuredfood.ingredient_properties4 import (
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
)
from measuredfood.utils.rawingredient3\
    .transform_nutrient_name_usda_to_measuredfood \
    import transform_nutrient_name_usda_to_measuredfood
from measuredfood.utils.make_displayed_name import make_displayed_name


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
        displayed_name = make_displayed_name(
            self.name,
            self.id
        )
        return displayed_name

    @staticmethod
    def get_absolute_url():
        return reverse('list-nutrient-profiles')

    class Meta:
        ordering = ["name"]

    def get_detail_view_url(self):
        return "/nutrientprofile/%i/detail/" % self.id


# Add all the fields related to nutrition to the nutrient profile model.
for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:

    # Create a nutrient name for the measured food database based on the
    # nutrient name from the USDA API.
    nutrient_name_measuredfood = \
        transform_nutrient_name_usda_to_measuredfood(
            nutrient_dict['nutrient_name_usda_api'],
            nutrient_dict['id_nutrient_usda_api'],
        )

    # Add the nutrient fields.
    NutrientProfile.add_to_class(
        nutrient_name_measuredfood,
        models.FloatField(
            blank=True,
            null=True,
            # The verbose_name is used to set the field labels in the ModelForm.
            verbose_name=nutrient_dict['nutrient_name_usda_api'],
        )
    )
    # Add the nutrient unit fields.
    NutrientProfile.add_to_class(
        nutrient_name_measuredfood+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['unit_nutrient_usda_api'],
                      nutrient_dict['unit_nutrient_usda_api']), ],
            blank=False,
            null=False,
            default=nutrient_dict['unit_nutrient_usda_api'],
            # The verbose_name is used to set the field labels in the ModelForm.
            verbose_name=nutrient_dict['nutrient_name_usda_api']+' unit',
        )
    )

    # Add all the fields related to tolerable upper intakes of each
    # nutrient to the nutrient profile model.
    # 'Max' is used to indicate 'maximum' because that is clearer than
    # 'tui' for
    # tolerable upper intake.

    # Add the nutrient fields.
    NutrientProfile.add_to_class(
        'max_'+nutrient_name_measuredfood,
        models.FloatField(
            blank=True,
            null=True,
            # The verbose_name is used to set the field labels in the ModelForm.
            verbose_name='max '+nutrient_dict['nutrient_name_usda_api'],
        )
    )
    # Add the nutrient unit fields.
    NutrientProfile.add_to_class(
        'max_'+nutrient_name_measuredfood+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['unit_nutrient_usda_api'],
                      nutrient_dict['unit_nutrient_usda_api']), ],
            blank=False,
            null=False,
            default=nutrient_dict['unit_nutrient_usda_api'],
            # The verbose_name is used to set the field labels in the ModelForm.
            verbose_name='max '+nutrient_dict['nutrient_name_usda_api']+' unit',
        )
    )
