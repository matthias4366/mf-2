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

    # In kg.
    current_weight = models.DecimalField(
        max_digits=5,
        decimal_places=0
    )
    UNIT_CURRENT_WEIGHT_CHOICES = [
        ('kg', 'kg'),
    ]
    unit_current_weight = models.CharField(
        max_length=10,
        choices=UNIT_CURRENT_WEIGHT_CHOICES,
        default='kg',
    )

    EXERISE_AMOUNT_CHOICES = [
        ('sedentary', 'sedentary'),
        ('endurance', 'endurance'),
        ('strength training', 'strength training'),
    ]
    exercise_amount = models.CharField(
        max_length=30,
        choices=EXERISE_AMOUNT_CHOICES
    )
