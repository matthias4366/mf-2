from django.contrib import admin
from .models import (
    RawIngredient,
    SpecificIngredient,
    NutrientProfile,
    Recipe,
    FullDayOfEating,
    Mealplan
    )

# Register your models here.
admin.site.register(RawIngredient)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(Recipe)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
