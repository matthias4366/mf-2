from django.contrib import admin
from learn_forms.models import (
    Programmer,
    Language
)

# Register your models here.
admin.site.register(Programmer)
admin.site.register(Language)
