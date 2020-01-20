from django.db import models
from django.contrib.auth.models import User

# TODO: Delete this file once it is obsolete.
"""
This is a model from the django-haystack tutorial found at
https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html 

It has nothing to do with measured food. It is for the purpose of learning 
django-haystack.
"""


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
