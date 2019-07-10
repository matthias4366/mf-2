from django.contrib import admin
from .models import (
    RawIngredient,
    SpecificIngredient,
    NutrientProfile,
    Recipe
    )

# Register your models here.
admin.site.register(RawIngredient)
admin.site.register(SpecificIngredient)
admin.site.register(NutrientProfile)
admin.site.register(Recipe)
