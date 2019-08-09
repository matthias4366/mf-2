from django.contrib import admin
from .models import (
    RawIngredient,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan
    )

# Register your models here.
admin.site.register(RawIngredient)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
