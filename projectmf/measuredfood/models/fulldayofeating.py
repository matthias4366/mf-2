from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from string import ascii_lowercase
from .nutrientprofile import NutrientProfile
from .nutrienttargetselection import NutrientTargetSelection
from .tolerableupperintake import TolerableUpperIntake

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6


class FullDayOfEating(models.Model):
    """
    Putting many recipes and single ingredients together creates a full day of
    eating.
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
        on_delete=models.PROTECT,
        editable = True,
        null=True,
        blank=False
    )

    # Within the nutrient profile, some nutrients are selected for the
    # mathematical calculation of the ingredient amounts in the final recipe.
    nutrient_target_selection = models.ForeignKey(
        NutrientTargetSelection,
        on_delete = models.PROTECT,
        editable = True,
        null = True,
        blank = False,
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
