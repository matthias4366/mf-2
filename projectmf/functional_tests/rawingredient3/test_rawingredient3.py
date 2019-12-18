from functional_tests.utils.click_navbar_item import \
    click_navbar_item
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.base import (
    # FunctionalTest,
    FunctionalTestWithUserLoggedIn)
from selenium.webdriver.common.keys import Keys
import time
from measuredfood.models import RawIngredient3
from django.contrib.auth.models import User
# python manage.py test functional_tests.rawingredient3.test_rawingredient3


class RawIngredient3Test(FunctionalTestWithUserLoggedIn):

    def test_get_from_food_data_central_carbohydrate_without_fiber(self):
        """
        The ingredients from the FoodData Central database have their
        carbohydrates stored as "Carbohydrate, by difference". This value
        includes fiber, which is not desired. Hence, from "Carbohydrate,
        by difference" and "Fiber, total dietary",
        "carbohydrate_without_fiber" is calculated.

        It is tested whether the carbohydrate_without_fiber value is
        calculated correctly for a food that has values for both
        "Carbohydrate, by difference" and "Fiber, total dietary".

        This test does not cover the calculation for the case that
        "Carbohydrate, by difference" is None and "Fiber, total dietary" is a
        positive number.
        :return:
        """

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
            )

        ingredient = {
            'id_ingredient_usda_api': '169738',
            'ingredient_name_usda_api':
                'Pasta, whole-wheat, dry (Includes foods '
                'for USDA\'s Food Distribution Program)',
        }

        # Simulate clicking on "Add ingredient using the FoodData Central
        # database (recommended)"
        self.browser.find_element_by_id(
            'id_button_get_from_food_data_central'
        ).click()

        self.browser.find_element_by_id(
            'id_FDC_ID'
        ).clear()

        self.browser.find_element_by_id(
            'id_FDC_ID'
        ).send_keys(
            str(ingredient['id_ingredient_usda_api'])
        )

        self.browser.find_element_by_id(
            'id_button_get_from_food_data_central'
        ).click()
        time.sleep(5)

        # Click the Edit button of the RawIngredient3 that was just created
        # using the FoodData Central database in order to check its properties.

        self.browser.find_element_by_id(
            'edit '+ingredient['ingredient_name_usda_api']
        ).click()

        carbohydrate_without_fiber_amount = self.browser.find_element_by_id(
            'id_carbohydrate_without_fiber-name-1-id'
        ).get_attribute('value')

        # If there is no value for the carbohydrate_without_fiber_amount,
        # the string is empty.
        if len(carbohydrate_without_fiber_amount) < 1:
            self.fail('carbohydrate_without_fiber_amount is an empty string.')
        else:
            carbohydrate_without_fiber_amount = \
                float(carbohydrate_without_fiber_amount)

        carbohyrate_by_difference = 73.37
        fiber_total_dietary = 9.2
        carbohydrate_without_fiber_desired_value = \
            carbohyrate_by_difference \
            - fiber_total_dietary

        self.assertAlmostEqual(
            carbohydrate_without_fiber_amount,
            carbohydrate_without_fiber_desired_value,
        )
