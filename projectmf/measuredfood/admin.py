from django.contrib import admin
from .models import (
    RawIngredient3,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan,
    SpecificNutrientTarget,
    UserProfile,
    InformationForNutrientProfile,
    FullDayOfEating2,
    SpecificIngredient2,
    )

# Register your models here.
admin.site.register(RawIngredient3)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
admin.site.register(SpecificNutrientTarget)
admin.site.register(UserProfile)
admin.site.register(InformationForNutrientProfile)
admin.site.register(FullDayOfEating2)
admin.site.register(SpecificIngredient2)
