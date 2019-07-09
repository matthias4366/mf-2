from django.contrib import admin
from .models import (
    RawIngredient,
    NutrientProfile
    )

# Register your models here.
admin.site.register(RawIngredient)
admin.site.register(NutrientProfile)
