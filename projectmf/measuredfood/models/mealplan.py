from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .nutrientprofile import NutrientProfile
from measuredfood.utils.make_displayed_name import make_displayed_name


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

    def __str__(self):
        displayed_name = make_displayed_name(
            self.name,
            self.id
        )
        return displayed_name

    @staticmethod
    def get_absolute_url():
        return reverse('list-mealplan')

    def get_detail_view_url(self):
        return "/mealplan/%i/detail/" % self.id

    class Meta:
        ordering = ["name"]
