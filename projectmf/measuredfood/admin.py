from django.contrib import admin
from .models import (
    RawIngredient3,
    SpecificIngredient,
    NutrientProfile,
    FullDayOfEating,
    Mealplan,
    SpecificNutrientTarget,
    Note,
    )

# Register your models here.
admin.site.register(RawIngredient3)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(FullDayOfEating)
admin.site.register(Mealplan)
admin.site.register(SpecificNutrientTarget)

# TODO: Remove the Note model once it is no longer needed. It is used solely
#  to learn to use search with Haystack and Whoosh.
admin.site.register(Note)
