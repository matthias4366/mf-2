import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from django.test import TestCase

# Run the unit tests using
# python manage.py test measuredfood.tests.test_calculate_ingredient_amount_slsqp.CalculateIngredientAmountSLSQPTest.test_calculate_ingredient_amount_slsqp
import pprint
from measuredfood.utils.fulldayofeating2.calculate_ingredient_amount_slsqp \
    import calculate_ingredient_amount_slsqp
from measuredfood.utils.fulldayofeating2\
    .calculate_ingredient_amount_slsqp_minimal \
    import calculate_ingredient_amount_slsqp_minimal_2

from measuredfood.models import (
    NutrientProfile,
    UserProfile,
    FullDayOfEating2,
    SpecificIngredient2,
    RawIngredient3,
)
from django.contrib.auth.models import User
from scipy.optimize import minimize
import numpy as np


class CalculateIngredientAmountSLSQPTest(TestCase):

    def test_calculate_ingredient_amount_slsqp(self):

        # Is a User object necessary? The FullDayOfEating2 and
        # SpecificIngredient2 objects do not need it. The NutrientProfile
        # model might need it.

        # Make the NutrientProfile object.

        # Make the RawIngredient3 objects.

        # Make the FullDayOfEating2 object.

        # Make the SpecificIngredient2 objects.

        calculate_ingredient_amount_slsqp_minimal_2(
            minimize=minimize,
            np=np,
        )

        self.fail('Finish the test calculate ingredient amount SLSQP')

