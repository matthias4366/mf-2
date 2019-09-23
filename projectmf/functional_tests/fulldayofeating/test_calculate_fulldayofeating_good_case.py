from selenium.webdriver.support.ui import Select
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from ..base import FunctionalTestWithUserLoggedIn
from selenium.webdriver.common.keys import Keys
import time
# from selenium.common.exceptions import NoSuchElementException
# from functional_tests.utils.check_exists_by_xpath \
#     import check_exists_by_xpath
from measuredfood.models import (
    FullDayOfEating,
    NutrientProfile,
)
from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User
from data.ingredients_data2 import ingredient_dict_list
from measuredfood.models import RawIngredient2

# import the ingredient dictionaries
import sys

sys.path.insert(0, '/projectmf/data/')


class FullDayOfEatingGoodCaseTest(FunctionalTestWithUserLoggedIn):

    def test_calculate_full_day_of_eating_good_case(self):
        """
        A lot of tests have been written to test for different errors that
        can occur in the calculation of a full day of eating.
        In this test, the good case is tested: everything is set up properly
        and it is tested whether the proper results are displayed.
        """
        pass
