from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import os

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()
