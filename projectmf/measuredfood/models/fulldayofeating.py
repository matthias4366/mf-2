from django.db import models
from django.contrib.auth.models import User
from .nutrientprofile import NutrientProfile
from measuredfood.utils.make_displayed_name import make_displayed_name


class FullDayOfEating(models.Model):
    """
    Putting many recipes and single ingredients together creates a full day of
    eating.
    """

    name = models.CharField(max_length=100)

    cooking_instruction = models.TextField(
        null=True,
        blank=True
    )

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
        on_delete=models.SET_NULL,
        editable=True,
        null=True,
        blank=False
    )

    def __str__(self):
        displayed_name = make_displayed_name(
            self.name,
            self.id
        )
        return displayed_name

    def get_detail_view_url(self):
        return "/fulldayofeating/%i/detail/" % self.id

    class Meta:
        ordering = ["name"]
