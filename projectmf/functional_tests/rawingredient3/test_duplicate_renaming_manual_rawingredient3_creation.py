from functional_tests.utils.click_navbar_item import \
    click_navbar_item
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.base import (
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

    def test_duplicate_renaming_manual_rawingredient3_creation(self):
        """
        A user manually creates a RawIngredient3 that already exists in
        their
        RawIngredient3 objects. The new RawIngredient3 object's name should
        be changed. For example, "Pasta" should be changed to "Pasta1".
        """

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
        )

        original_name = 'Pasta 4540'
        expected_duplicate_name = 'Pasta 4541'

        # Make the original ingredient.
        self.browser.find_element_by_id(
            'id_button_new_rawingredient3'
        ).click()
        self.browser.find_element_by_id('id_name').send_keys(original_name)
        self.browser.find_element_by_id(
            'id_button_save_new_rawingredient3').click()

        # Make exactly the same ingredient again.
        self.browser.find_element_by_id(
            'id_button_new_rawingredient3'
        ).click()
        self.browser.find_element_by_id('id_name').send_keys(original_name)
        self.browser.find_element_by_id(
            'id_button_save_new_rawingredient3').click()

        ingredients_with_original_name = self.browser.find_elements_by_id(
            'edit '+original_name
        )
        n_ingredients_with_original_name = len(ingredients_with_original_name)
        self.assertEqual(n_ingredients_with_original_name, 1)

        ingredients_with_name_of_duplicate = self.browser.find_elements_by_id(
            'edit '+expected_duplicate_name
        )
        n_ingredients_with_name_of_duplicate = len(
            ingredients_with_name_of_duplicate
        )
        self.assertEqual(n_ingredients_with_name_of_duplicate, 1)

        # Create the ingredient with the original name again.
        # An ingredient with the next higher number already exists.
        # Therefore, the name of the added ingredient should be the original
        # name + '2'.

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
        )

        # Make the original ingredient for the third time.
        self.browser.find_element_by_id(
            'id_button_new_rawingredient3'
        ).click()
        self.browser.find_element_by_id('id_name').send_keys(original_name)
        self.browser.find_element_by_id(
            'id_button_save_new_rawingredient3').click()

        ingredients_with_original_name = self.browser.find_elements_by_id(
            'edit '+original_name
        )
        n_ingredients_with_original_name = len(ingredients_with_original_name)
        self.assertEqual(n_ingredients_with_original_name, 1)

        ingredients_with_name_of_duplicate = self.browser.find_elements_by_id(
            'edit '+expected_duplicate_name
        )
        n_ingredients_with_name_of_duplicate = len(
            ingredients_with_name_of_duplicate
        )
        self.assertEqual(n_ingredients_with_name_of_duplicate, 1)

        expected_duplicate2_name = 'Pasta 4542'

        ingredients_with_name_of_duplicate2 = self.browser.find_elements_by_id(
            'edit '+expected_duplicate2_name
        )
        n_ingredients_with_name_of_duplicate2 = len(
            ingredients_with_name_of_duplicate2
        )
        self.assertEqual(n_ingredients_with_name_of_duplicate2, 1)
