from django.db import models
from django.contrib.auth.models import User

MAX_DIGITS_ = 20
DECIMAL_PLACES_ = 6

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RawIngredient(models.Model):
    """
    10.6.2019. The RawIngredient model represents the raw ingredients.
    The user adds the ingredients themselves. They can't pull ingredients from
    a database or share ingredients with other users (yet). These ingredients
    serve as the basis for creating recipes.
    """
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    calories = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True
    )


class FullDayOfEating(models.Model):
    name = models.CharField(max_length=20)


class SpecificIngredient(models.Model):

    base_amount = models.DecimalField(
        max_digits=MAX_DIGITS_,
        decimal_places=DECIMAL_PLACES_,
        blank=True,
        null=True
    )

    fulldayofeating = models.ForeignKey(
        FullDayOfEating,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    rawingredient = models.ForeignKey(
        RawIngredient,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        label = 'Specific version of ' + self.rawingredient.name
        return label
