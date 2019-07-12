from django.contrib import admin
from learn_forms.models import (
    Programmer,
    Language,
    RawIngredient,
    SpecificIngredient,
    FullDayOfEating
)

# Register your models here.
admin.site.register(Programmer)
admin.site.register(Language)
admin.site.register(RawIngredient)
admin.site.register(SpecificIngredient)
admin.site.register(FullDayOfEating)
