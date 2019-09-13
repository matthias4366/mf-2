from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.initial_nutrient_profiles import nutrient_profile_dict_list
from .base import FunctionalTestWithUserLoggedIn
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from functional_tests.utils.check_exists_by_xpath \
    import check_exists_by_xpath
from measuredfood.models import NutrientProfile
from django.contrib.auth.models import User

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class TolerableUpperIntakeTest(FunctionalTestWithUserLoggedIn):

    pass
