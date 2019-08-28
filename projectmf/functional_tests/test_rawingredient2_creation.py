from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.ingredients_data2 import ingredient_dict_list
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class RawIngredientTest(FunctionalTest):

    def test_user_registration_and_rawingredient_creation(self):
        """
        There should be a temporary database created for testing purposes only.
        Test the registration of a new user with a username and a password.
        """

        dummy_username = 'DummyUser'
        dummy_email = 'DummyUser@gmail.com'
        dummy_password = 'testpassword'

        # Open the registration page
        self.browser.get(self.live_server_url + '/register/')

        # Find elements by name
        username = self.browser.find_element_by_name('username')
        email = self.browser.find_element_by_name('email')
        password1 = self.browser.find_element_by_name('password1')
        password2 = self.browser.find_element_by_name('password2')

        # Input values into the fields
        username.send_keys(dummy_username)
        email.send_keys(dummy_email)
        password1.send_keys(dummy_password)
        password2.send_keys(dummy_password)
        time.sleep(3)

        # Simulate clicking on Sign Up
        sign_up_button = self.browser.find_element_by_id('id_button_signup')
        sign_up_button.send_keys(Keys.ENTER)

        # TODO: Check if the user has been added to the database.

        # A redirect to the login page should happen at this point.
        # TODO: Test whether the redirect has happened.

        time.sleep(3)

        # Find login elements
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')

        # Input values into the fields
        username_field.send_keys(dummy_username)
        password_field.send_keys(dummy_password)

        # Simulate clicking on Log In
        click_navbar_item(
            'id_button_login',
            self.browser,
            Keys,
            )

        time.sleep(3)

        # A redirect to the homepage should happen at this point.
        # TODO: Test whether a redirect to the homepage happens.

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            )

        time.sleep(3)

        # Add all the ingredients
        # for k in range(len(ingredient_dict_list)):
        # It is not necessary to add all the ingredients.
        for k in range(2):

            new_ingredient_button = self.browser.find_element_by_id(
                'id_button_new_rawingredient2'
            )
            new_ingredient_button.send_keys(Keys.ENTER)

            time.sleep(1)

            for key, value in ingredient_dict_list[k].items():
                if value is not None:
                    self.browser.find_element_by_name(key).send_keys(str(value))

            # Simulate clicking the save button
            save_button = self.browser.find_element_by_id(
                'id_button_save_new_rawingredient2'
            )
            save_button.send_keys(Keys.ENTER)

            time.sleep(1)
