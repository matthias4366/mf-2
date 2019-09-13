from django.db import models
from django.contrib.auth.models import User
from measuredfood.ingredient_properties2 import (
    VITAMINS_AND_DEFAULT_UNITS,
    ELEMENTS_AND_DEFAULT_UNITS,
)


class TolerableUpperIntake(models.Model):
    """
    Some vitamins or other nutrients are toxic when an excessive amount is
    ingested. The tolerable upper intake levels of the nutrients are stored
    in this model.
    The tolerable upper intakes are taken from the National Institute of Health.
    Source:
    https://ods.od.nih.gov/Health_Information/Dietary_Reference_Intakes.aspx

    The source says: Source of intake should be from food only to prevent high
    intakes. Therefore, where the source says the tolerable upper intake is
    not determined, that does not mean "eat as much as you want no problem".
    It means "there certainly is a tolerable upper intake level. However, due
    to a lack of data we do not know where it is." There are also some vitamins
    and elements that due to their water solubility are less critical: you can
    just pee out the excess.
    """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # TODO: The null and blank settings might be wrong as I have not used
        #       them for the other models.
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.name

    # TODO: activate this code when you have a url for
    #  'list-tolerableupperintake'
    # def get_absolute_url(self):
    #     return reverse('list-tolerableupperintake')


# Vitamins
for nutrient_dict in VITAMINS_AND_DEFAULT_UNITS:
    # Add the fields with the tolerable upper intake of each vitamin.
    TolerableUpperIntake.add_to_class(
        nutrient_dict['name']+'_tolerable_upper_intake',
        models.FloatField(
            blank=True,
            null=True
        )
    )
    # Add the fields with the units of the vitamins.
    TolerableUpperIntake.add_to_class(
        nutrient_dict['name']+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['default_unit'], nutrient_dict[
                'default_unit']), ],
            blank=False,
            null=False,
            default=nutrient_dict['default_unit'],
        )
    )

# Elements
for nutrient_dict in ELEMENTS_AND_DEFAULT_UNITS:
    # Add the fields with the tolerable upper intake of each elements.
    TolerableUpperIntake.add_to_class(
        nutrient_dict['name']+'_tolerable_upper_intake',
        models.FloatField(
            blank=True,
            null=True
        )
    )
    # Add the fields with the units of the elements.
    TolerableUpperIntake.add_to_class(
        nutrient_dict['name']+'_unit',
        models.CharField(
            max_length=100,
            choices=[(nutrient_dict['default_unit'], nutrient_dict[
                'default_unit']), ],
            blank=False,
            null=False,
            default=nutrient_dict['default_unit'],
        )
    )
