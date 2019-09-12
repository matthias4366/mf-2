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

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')
# import logging


class NutrientProfileTest(FunctionalTestWithUserLoggedIn):

    def test_nutrient_profile_creation_with_valid_data(self):
        """
        Test the creation of a nutrient profile where everything goes as it
        should, i.e. all the required fields are filled out.
        """

        # Simulate clicking on nutrient profiles
        click_navbar_item(
            'id_menu_item_nutrient_profiles',
            self.browser,
            Keys,
            time,
            )

        time.sleep(0.1)

        # Add the first nutrient profile from the list of nutrient profiles
        # saved in the fixtures.

        new_nutrient_profile_button = self.browser.find_element_by_id(
            'id_button_new_nutrient_profile'
        )
        new_nutrient_profile_button.click()

        time.sleep(0.1)

        k = 0

        for key, value in nutrient_profile_dict_list[k].items():
            id_from_key = 'id_' + key
            # logging.info('\n id_from_key in
            # test_nutrient_profile_creation '
            #              '\n')
            # logging.info(id_from_key)
            # logging.info('\n value in test_nutrient_profile_creation '
            #              '\n')
            # logging.info(value)
            if value is not None:

                self.browser.find_element_by_id(id_from_key).send_keys(
                    str(value)
                )

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_nutrientprofile'
        )
        save_button.click()

        time.sleep(1)

        # Test whether the saved nutrient profile shows up in the list of
        # nutrient profiles.

        xpath_ = "//*[contains(text(), " \
                 "'Maintenance plus vitamins from NIH Males 19-30')]"

        nutrient_profile_is_shown_in_list = check_exists_by_xpath(
            self.browser,
            xpath_,
            NoSuchElementException
        )

        self.assertTrue(nutrient_profile_is_shown_in_list)

        # Test whether the saved nutrient profile is in the database.
        nutrient_profile_query = NutrientProfile.objects.filter(
            name=nutrient_profile_dict_list[k]['name']
        )
        nutrient_profile_was_saved = nutrient_profile_query.exists()
        self.assertTrue(nutrient_profile_was_saved)
