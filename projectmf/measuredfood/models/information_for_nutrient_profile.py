from django.db import models
from django.contrib.auth.models import User


class InformationForNutrientProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.DecimalField(max_digits=5, decimal_places=0)

    BIOLOGICAL_SEX_CHOICES = [
        ('female', 'female'),
        ('male', 'male'),
    ]
    biological_sex = models.CharField(
        max_length=10,
        choices=BIOLOGICAL_SEX_CHOICES
    )

    is_pregnant = models.BooleanField()
    is_lactating = models.BooleanField()

    WEIGHT_CHANGE_CHOICES = [
        ('lose weight fast', -500),
        ('lose weight slow', -250),
        ('maintain weight', 0),
        ('gain weight slow', 250),
        ('gain weight fast', 500),
    ]
    weight_change = models.DecimalField(
        decimal_places=0,
        max_digits=20,
        choices=WEIGHT_CHANGE_CHOICES
    )

    # Total body mass in kg.
    bodymass = models.DecimalField(
        max_digits=5,
        decimal_places=0
    )
    UNIT_BODYMASS_CHOICES = [
        ('kg', 'kg'),
    ]
    unit_bodymass = models.CharField(
        max_length=10,
        choices=UNIT_BODYMASS_CHOICES,
        default='kg',
    )

    ACTIVITY_LEVEL_CHOICES = [
        ('Sedentary', 'Sedentary'),
        ('Light Exercise', 'Light Exercise'),
        ('Moderate Exercise', 'Moderate Exercise'),
        ('Heavy Exercise', 'Heavy Exercise'),
        ('Athlete', 'Athlete'),
    ]

    activity_level = models.CharField(
        max_length=30,
        choices=ACTIVITY_LEVEL_CHOICES,
        null=True,
    )
