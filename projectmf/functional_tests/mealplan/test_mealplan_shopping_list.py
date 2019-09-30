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


class MealplanShoppingListTest(FunctionalTestWithUserLoggedIn):

    @unittest.skip('Skip. Finish writing this test later.')
    def test_shopping_list_mealplan(self):
        """
        Test whether the shopping list is created correctly.
        """

        """
        Implementation:

        Create two full days of eating.

        The nutrient profile does not matter at all. Make an empty,
        dummy profile.

        Set all the scaling options to 'fixed'. This way, the comparison
        values for the shopping list can be derived straightforwardly from
        the input values for the test.
        
        """

        #

        """

        Create a mealplan.

        Simulate clicking 'Create shopping list'.

        Assert that the values in the shopping list are equal to the
        comparison values.

        Find the values in the shopping list by id. Set the ids in the template.

        Keep the ceiling function in mind. Use some numbers with decimal
        digits as input values (such as 1.45).

        """
        self.fail('Finish the test!')
