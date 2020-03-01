from haystack import indexes
from measuredfood.models import (
    FullDayOfEating,
    NutrientProfile,
    Mealplan,
    RawIngredient3,
)


# Link to the tutorial:
# https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html


class FullDayOfEatingIndex(indexes.SearchIndex, indexes.Indexable):
    """
    A search index for the FullDayOfEating model. For starters, the focus
    will be on finding a FullDayOfEating object using the name.
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return FullDayOfEating

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # TODO: Here is probably where you can implement the function of
        #  users being able to keep their FullDayOfEating objects private.
        return self.get_model().objects.all()


class NutrientProfileIndex(indexes.SearchIndex, indexes.Indexable):
    """
    A search index for the FullDayOfEating model. For starters, the focus
    will be on finding a FullDayOfEating object using the name.
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return NutrientProfile

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # TODO: Here is probably where you can implement the function of
        #  users being able to keep their FullDayOfEating objects private.
        return self.get_model().objects.all()


class MealplanIndex(indexes.SearchIndex, indexes.Indexable):
    """
    A search index for the FullDayOfEating model. For starters, the focus
    will be on finding a FullDayOfEating object using the name.
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Mealplan

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # TODO: Here is probably where you can implement the function of
        #  users being able to keep their FullDayOfEating objects private.
        return self.get_model().objects.all()


class RawIngredient3Index(indexes.SearchIndex, indexes.Indexable):
    """
    A search index for the FullDayOfEating model. For starters, the focus
    will be on finding a FullDayOfEating object using the name.
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return RawIngredient3

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # TODO: Here is probably where you can implement the function of
        #  users being able to keep their FullDayOfEating objects private.
        return self.get_model().objects.all()


