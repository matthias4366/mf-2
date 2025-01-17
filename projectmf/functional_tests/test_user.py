from django.contrib.auth.models import User
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from functional_tests.base import wait

import sys
sys.path.insert(0, '/projectmf/data/')


class NewUserProfileTest(FunctionalTest):

    @wait
    def test_user_registration(self):

        dummy_username = 'DummyUser1'
        dummy_email = 'DummyUser1@gmail.com'
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

        # Check if the dummy user object exists in the database.
        query_dummy_user = User.objects.filter(
            username=dummy_username,
        )

        dummy_user_exists = query_dummy_user.exists()

        self.assertTrue(dummy_user_exists)
