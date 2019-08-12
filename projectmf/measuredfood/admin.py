from django.contrib import admin
from .models import (
    RawIngredient,
    RawIngredient2,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan
    )

# Register your models here.
admin.site.register(RawIngredient)
admin.site.register(RawIngredient2)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
