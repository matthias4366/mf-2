from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.initial_nutrient_profiles import nutrient_profile_dict_list
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')
# import logging


class NutrientProfileTest(FunctionalTest):

    def test_nutrient_profile_creation(self):
        """
        Every test starts with a user registration. It might make sense to work
        on speeding it up.
        Test the creation of a nutrient profile.
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

        click_navbar_item(
            'id_button_signup',
            self.browser,
            Keys,
            time,
            )

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
        log_in_button = self.browser.find_element_by_id('id_button_login')
        log_in_button.send_keys(Keys.ENTER)

        time.sleep(3)

        # Simulate clicking on nutrient profiles
        click_navbar_item(
            'id_menu_item_nutrient_profiles',
            self.browser,
            Keys,
            time,
            )

        time.sleep(3)

        # Add all the nutrient profiles
        for k in range(len(nutrient_profile_dict_list)):

            new_nutrient_profile_button = self.browser.find_element_by_id(
                'id_button_new_nutrient_profile'
            )
            new_nutrient_profile_button.send_keys(Keys.ENTER)

            time.sleep(1)

            for key, value in nutrient_profile_dict_list[k].items():
                id_from_key = 'id_' + key
                # logging.info('\n id_from_key in
                # test_nutrient_profile_creation '
                #              '\n')
                # logging.info(id_from_key)
                # logging.info('\n value in test_nutrient_profile_creation '
                #              '\n')
                # logging.info(value)
                if value is not None:

                    self.browser.find_element_by_id(id_from_key).send_keys(
                        str(value)
                    )

            # Simulate clicking the save button
            save_button = self.browser.find_element_by_id(
                'id_button_save_new_nutrientprofile'
            )
            save_button.send_keys(Keys.ENTER)

            time.sleep(1)
