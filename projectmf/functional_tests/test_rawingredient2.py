from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.ingredients_data2 import ingredient_dict_list
from .base import (
    # FunctionalTest,
    FunctionalTestWithUserLoggedIn)
from selenium.webdriver.common.keys import Keys
import time
from measuredfood.models import RawIngredient2
# from functional_tests.base import wait


# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class RawIngredient2Test(FunctionalTestWithUserLoggedIn):

    def test_rawingredient2_creation(self):

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
            )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.
        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.send_keys(Keys.ENTER)

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.send_keys(Keys.ENTER)

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public':
                if value is not None:
                    self.browser. \
                        find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

    def test_rawingredient2_creation_invalid_input(self):
        """
        When filling out the creation form for the RawIngredient2, the "name"
        field is necessary. It is tested that the user can not add a new
        RawIngredient2 without a "name".
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.
        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.send_keys(Keys.ENTER)

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.send_keys(Keys.ENTER)

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            # The name is left blank on purpose, which is expected to
            # impede the creation of a RawIngredient2 instance.
            if key != 'is_public' and key != 'name':
                if value is not None:
                    self.browser. \
                        find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertFalse(rawingredient2_was_saved)
