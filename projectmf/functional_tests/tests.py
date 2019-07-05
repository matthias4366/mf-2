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
        username = self.browser.find_element_by_name('username')
        username.send_keys('DummyUser')
        # username.submit()
        time.sleep(3)
