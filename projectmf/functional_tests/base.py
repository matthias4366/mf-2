from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import os
from selenium.common.exceptions import WebDriverException

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


MAX_WAIT = 10


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

        # TODO: Create a dummy user and log them in.

    def tearDown(self):
        # time.sleep(3)
        self.browser.quit()


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
