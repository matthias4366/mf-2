from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from string import ascii_lowercase
from .nutrientprofile import NutrientProfile
from .fulldayofeating import FullDayOfEating
from .tolerableupperintake import TolerableUpperIntake

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class Mealplan(models.Model):
    """
    Putting many SpecificFullDayOfEating instances together creates a mealplan.
    """

    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Every full day of eating is linked with one nutrient_profile.
    # But one nutrient_profile can be linked to many full days of eating.
    nutrient_profile = models.ForeignKey(
        NutrientProfile,
        on_delete=models.PROTECT,
        editable = True,
        null=True,
        blank=False
    )

    tolerable_upper_intake = models.ForeignKey(
        TolerableUpperIntake,
        on_delete = models.PROTECT,
        editable = True,
        null = True,
        blank = False,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-mealplan')
