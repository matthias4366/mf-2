from functional_tests.utils.click_navbar_item import \
    click_navbar_item
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.base import (
    # FunctionalTest,
    FunctionalTestWithUserLoggedIn
)
from selenium.webdriver.common.keys import Keys
import time
import unittest

# from django.contrib.auth.models import User
# python manage.py test functional_tests.rawingredient3.test_rawingredient3

@unittest.skip('Duplicate renaming no longer necessary since the ID\'s '
               'are shown as well.')
class RawIngredient3Test(FunctionalTestWithUserLoggedIn):

    def test_duplicate_renaming_get_rawingredient3_food_data_central(self):
        """
        A user gets a RawIngredient3 object from the FoodData Central
        database that already exists in their RawIngredient3 objects. Test if
        the new RawIngredient3 object gets renamed correctly. For example,
        "Pasta" should be changed to "Pasta1".

        (!): This test does not test whether "Pasta1" gets renamed to "Pasta2".
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

        # Check if there is the original ingredient, and that there is no
        # duplication of the same ingredient.
        # Check if the duplicate ingredient has been properly renamed.

        renamed_ingredient_name = ingredient['ingredient_name_usda_api'] + '1'

        ingredients_with_original_name = self.browser.find_elements_by_id(
            'edit '+ingredient['ingredient_name_usda_api']
        )
        n_ingredients_with_original_name = len(ingredients_with_original_name)
        self.assertEqual(n_ingredients_with_original_name, 1)

        ingredients_with_adapted_name = self.browser.find_elements_by_id(
            'edit '+renamed_ingredient_name
        )
        n_ingredients_with_adapted_name = len(ingredients_with_adapted_name)
        self.assertEqual(n_ingredients_with_adapted_name, 1)
