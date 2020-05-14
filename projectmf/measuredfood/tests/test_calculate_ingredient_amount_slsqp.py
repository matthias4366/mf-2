import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from django.test import TestCase

# Run the unit tests using
# python manage.py test measuredfood.tests
import pprint
from measuredfood.utils.nutrient_profile.nutrientprofile_make_for_user import \
    nutrientprofile_make_for_user
from \
    measuredfood.utils.nutrient_profile\
    .calculate_total_daily_energy_expenditure \
    import calculate_total_daily_energy_expenditure

from measuredfood.models import (
    NutrientProfile,
    UserProfile,
    FullDayOfEating,
)
from django.contrib.auth.models import User


class CalculateIngredientAmountSLSQPTest(TestCase):

    def test_calculate_ingredient_amount_slsqp(self):

        self.assertEqual('correct', )
