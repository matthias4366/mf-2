# from functional_tests.utils.click_navbar_item import \
#     click_navbar_item
# from selenium.webdriver.support.ui import Select
# from django.contrib.auth.models import User
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.base import (
    # FunctionalTest,
    FunctionalTestWithUserLoggedIn
)
# from selenium.webdriver.common.keys import Keys
# import time
# from measuredfood.models import (
#     NutrientProfile,
#     FullDayOfEating,
# )

# from django.contrib.auth.models import User
# python manage.py test functional_tests.rawingredient3.test_rawingredient3
import unittest

@unittest.skip('Duplicate renaming no longer necessary since the ID\'s '
               'are shown as well.')
class RawIngredient3Test(FunctionalTestWithUserLoggedIn):

    def test_duplicate_renaming_of_fulldayofeating_create_fulldayofeating(self):
        """
        A user manually creates a new FullDayOfEating object. There
        already exists a FullDayOfEating object with the same name in their
        FullDayOfEating objects.

        Test if the new FullDayOfEating object gets renamed appropriately.
        "Stir fry" should become "Stir fry2".
        """
        self.fail('Finish the test!')
