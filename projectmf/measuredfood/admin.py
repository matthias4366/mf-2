from django.contrib import admin
from .models import (
    RawIngredient2,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan,
    NutrientTargetSelection,
    TolerableUpperIntake,
    SpecificNutrientTarget,
    )

# Register your models here.
admin.site.register(RawIngredient2)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
admin.site.register(NutrientTargetSelection)
admin.site.register(TolerableUpperIntake)
admin.site.register(SpecificNutrientTarget)
