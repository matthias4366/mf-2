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

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()
