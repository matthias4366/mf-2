from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .nutrientprofile import NutrientProfile


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
        on_delete=models.SET_NULL,
        editable=True,
        null=True,
        blank=False
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('list-mealplan')

    class Meta:
        ordering = ["name"]
