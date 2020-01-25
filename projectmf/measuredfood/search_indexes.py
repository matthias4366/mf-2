import datetime
from haystack import indexes
from measuredfood.models import Note
from measuredfood.models import FullDayOfEating


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    # TODO: Delete the class NoteIndex once it is obsolete.
    """
    This is a class from the django-haystack tutorial found at
    https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html

    It has nothing to do with measured food. It is for the purpose of learning
    django-haystack.
    """
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            pub_date__lte=datetime.datetime.now()
        )


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
