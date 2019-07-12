from django.shortcuts import render, redirect
from .models import Programmer, Language
from django.forms import modelformset_factory, inlineformset_factory

# def index(request, programmer_id):
#     programmer = Programmer.objects.get(pk=programmer_id)
#     LanguageFormset = inlineformset_factory(Programmer, Language, fields=('__all__'), extra=1)
#
#     if request.method == 'POST':
#         formset = LanguageFormset(request.POST, instance=programmer)
#         if formset.is_valid():
#             formset.save()
#
#             return redirect('index', programmer_id=programmer.id)
#
#     formset = LanguageFormset(instance=programmer)
#
#     return render(request, 'index.html', {'formset': formset})

from .models import FullDayOfEating, SpecificIngredient

# Making an equivalent view for my models.
# Let's forget the raw ingredients for a second.
# The programmer is equivalent to the full day of eating.
# The language is equivalent to the specific ingredient.


def index(request, fulldayofeating_id):
    fulldayofeating = FullDayOfEating.objects.get(pk=fulldayofeating_id)
    SpecificIngredientFormset = inlineformset_factory(FullDayOfEating, SpecificIngredient, fields=('__all__'), extra=1)

    if request.method == 'POST':
        formset = SpecificIngredientFormset(request.POST, instance=fulldayofeating)
        if formset.is_valid():
            formset.save()

            return redirect('index', fulldayofeating_id=fulldayofeating.id)

    formset = SpecificIngredientFormset(instance=fulldayofeating)

    return render(request, 'index.html', {'formset': formset})


def basictable(request):
    return render(request, 'table.html')
