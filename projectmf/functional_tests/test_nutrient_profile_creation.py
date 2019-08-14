from .base import FunctionalTest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')
from data.ingredients_data import ingredient_dict_list
from data.initial_nutrient_profiles import nutrient_profile_dict_list

class NutrientProfileTest(FunctionalTest):

    def test_nutrient_profile_creation(self):
        """
        Every test starts with a user registration. It might make sense to work
        on speeding it up.
        Test the creation of a nutrient profile.
        """

        DUMMY_USERNAME = 'DummyUser'
        DUMMY_EMAIL = 'DummyUser@gmail.com'
        DUMMY_PASSWORD = 'testpassword'

        # Open the registration page
        self.browser.get(self.live_server_url + '/register/')

        # Find elements by name
        username = self.browser.find_element_by_name('username')
        email = self.browser.find_element_by_name('email')
        password1 = self.browser.find_element_by_name('password1')
        password2 = self.browser.find_element_by_name('password2')

        # Input values into the fields
        username.send_keys(DUMMY_USERNAME)
        email.send_keys(DUMMY_EMAIL)
        password1.send_keys(DUMMY_PASSWORD)
        password2.send_keys(DUMMY_PASSWORD)
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
        username_field.send_keys(DUMMY_USERNAME)
        password_field.send_keys(DUMMY_PASSWORD)

        # Simulate clicking on Log In
        log_in_button = self.browser.find_element_by_id('id_button_login')
        log_in_button.send_keys(Keys.ENTER)

        time.sleep(3)

        # Simulate clicking on nutrient profiles
        nutrient_profiles_menu_item = self.browser.find_element_by_id(
            'id_menu_item_nutrient_profiles')
        nutrient_profiles_menu_item.send_keys(Keys.ENTER)

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
                if value != None:
                    self.browser.find_element_by_id(id_from_key).send_keys(str(value))

            # Simulate clicking the save button
            save_button = self.browser.find_element_by_id(
                'id_button_save_new_nutrient_profile'
            )
            save_button.send_keys(Keys.ENTER)

            time.sleep(1)
