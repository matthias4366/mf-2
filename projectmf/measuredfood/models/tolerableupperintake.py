from django.db import models
from django.contrib.auth.models import User

class TolerableUpperIntake(models.Model):
    """
    Some vitamins or other nutrients are toxic when an excessive amount is
    ingested. The tolerable upper intake levels of the nutrients are stored
    in this model.
    For some nutrients, the US government hasn't established a tolerable upper
    intake as the nutrient is safe in any amount. That needs to be considered.
    """
    pass
