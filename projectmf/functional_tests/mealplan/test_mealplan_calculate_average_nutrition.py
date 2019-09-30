# from selenium.webdriver.support.ui import Select
# from functional_tests.utils.click_navbar_item import \
#     click_navbar_item
from ..base import FunctionalTestWithUserLoggedIn
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.common.exceptions import NoSuchElementException
# from functional_tests.utils.check_exists_by_xpath \
#     import check_exists_by_xpath
from measuredfood.models import (
    FullDayOfEating,
    NutrientProfile,
)
# from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User
# from data.ingredients_data2 import ingredient_dict_list
# from measuredfood.models import RawIngredient2
import unittest
# import the ingredient dictionaries
import sys

sys.path.insert(0, '/projectmf/data/')


class MealplanCalculateAverageNutritionTest(FunctionalTestWithUserLoggedIn):

    @unittest.skip('Skip. Finish writing this test later.')
    def test_mealplan_calculate_average_nutrition(self):
        """
        Test whether the average nutrition is calculated correctly.

        Do not test the correct calculation of:
        unit
        % target
        % max
        Judgment
        .
        These are tested as part of the fulldayofeating test suite found in
        functional_tests/fulldayofeating.

        It is not tested whether the calculation of a full day of eating
        works correctly.

        Implementation:

        Create a nutrient profile. It does not matter much. Use the
        'Maintenance EU' profile.

        Create two full days of eating.

        Calculate both of them.

        Capture the results from the html page.

        Calculate the average of the results, which will be the comparison
        values.

        Create a mealplan.

        Add the same nutrient profile to the mealplan which was used to
        calculate the full days of eating.

        Add both full days of eating to the mealplan.

        Calculate the average nutrition of the mealplan.

        Assert that the average nutrition values of the mealplan are equal to
        the comparison values.
        """
        self.fail('Finish the test!')
