from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10

DUMMY_USERNAME = 'DummyUser'
DUMMY_EMAIL = 'DummyUser@gmail.com'
DUMMY_PASSWORD = 'testpassword'


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_user_registration(self):
        """
        There should be a temporary database created for testing purposes only.
        Test the registration of a new user with a username and a password.
        """

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

        # A redirect to the homepage should happen at this point.
        # TODO: Test whether a redirect to the homepage happens.

        # Simulate clicking on the menu item "Ingredients"
        ingredients_menu_item = self.browser.find_element_by_id(
            'id_menu_item_ingredients')
        ingredients_menu_item.send_keys(Keys.ENTER)

        time.sleep(3)

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_ingredient'
        )
        new_ingredient_button.send_keys(Keys.ENTER)

        time.sleep(3)
