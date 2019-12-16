from django.contrib import admin
from .models import (
    RawIngredient3,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan,
    SpecificNutrientTarget,
    )

# Register your models here.
admin.site.register(RawIngredient3)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
admin.site.register(SpecificNutrientTarget)
