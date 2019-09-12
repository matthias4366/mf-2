from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from selenium import webdriver
import time
import os
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')

MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn


def wait_until_user_has_signed_up():
    pass


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        # time.sleep(3)
        self.browser.quit()


class FunctionalTestWithUserLoggedIn(StaticLiveServerTestCase):
    """
    For many test cases, it is necessary to have a user that is registered and
    logged in. This class provides a basis for such tests by taking care of
    user registration and login in the setUp method.
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

        # Create a new dummy user.
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

        # Simulate clicking on Sign Up
        sign_up_button = self.browser.find_element_by_id('id_button_signup')
        sign_up_button.send_keys(Keys.ENTER)

        time.sleep(0.5)

        # Check if the dummy user object exists in the database.
        query_dummy_user = User.objects.filter(
            username=dummy_username,
        )

        dummy_user_exists = query_dummy_user.exists()

        self.assertTrue(dummy_user_exists)

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
            time,
        )

    def tearDown(self):
        self.browser.quit()

