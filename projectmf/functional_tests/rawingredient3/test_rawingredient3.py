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
# from measuredfood.models import RawIngredient3
# from django.contrib.auth.models import User
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

    def test_duplicate_renaming_get_rawingredient3_food_data_central(self):
        """
        A user gets a RawIngredient3 object from the FoodData Central
        database that already exists in their RawIngredient3 objects. Test if
        the new RawIngredient3 object gets renamed correctly. For example,
        "Pasta" should be changed to "Pasta1".
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

    def test_duplicate_renaming_of_rawingredient3_copy_fulldayofeating(self):
        """
        A user copies a FullDayOfEating object from another user. As part of
        this, the RawIngredient3 objects are copied as well. Some of the new
        RawIngredient3 objects might already exist in the user's
        RawIngredient3 objects. Test if
        the new RawIngredient3 object gets renamed correctly. For example,
        "Pasta" should be changed to "Pasta1".
        """
        self.fail('Finish the test!')

    def test_duplicate_renaming_of_fulldayofeating_copy_fulldayofeating(self):
        """
        A user copies a FullDayOfEating object from another user. There
        already exists a FullDayOfEating object with the same name in their
        FullDayOfEating objects.

        Test if the new FullDayOfEating object gets renamed appropriately.
        "Stir fry" should become "Stir fry2".
        """
        self.fail('Finish the test!')

    def test_duplicate_renaming_of_fulldayofeating_create_fulldayofeating(self):
        """
        A user manually creates a new FullDayOfEating object. There
        already exists a FullDayOfEating object with the same name in their
        FullDayOfEating objects.

        Test if the new FullDayOfEating object gets renamed appropriately.
        "Stir fry" should become "Stir fry2".
        """
        self.fail('Finish the test!')
