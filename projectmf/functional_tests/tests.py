from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10


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
        username.send_keys('DummyUser')
        email.send_keys('DummyUser@gmail.com')
        password1.send_keys('testpassword')
        password2.send_keys('testpassword')

        # Simulate clicking on Sign Up
        sign_up_button = self.browser.find_element_by_id('id_button_signup')
        sign_up_button.send_keys(Keys.ENTER)
        # ['username', 'email', 'password1', 'password2']
        # username.submit()
        time.sleep(3)
