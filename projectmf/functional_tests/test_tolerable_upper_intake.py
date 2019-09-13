from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.initial_tolerable_upper_intake import initial_tolerable_upper_intake
from .base import FunctionalTestWithUserLoggedIn
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from functional_tests.utils.check_exists_by_xpath \
    import check_exists_by_xpath
from measuredfood.models import TolerableUpperIntake
# from django.contrib.auth.models import User

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class TolerableUpperIntakeTest(FunctionalTestWithUserLoggedIn):

    def test_tolerable_upper_intake_creation_with_valid_data(self):
        """
        Test of the creation of a TolerableUpperIntake object where the input
        data is valid. The test is successfull if the TolerableUpperIntake
        object has been created successfully.
        """

        # Simulate the clicking on the tolerable upper intakes navbar item.
        # Simulate clicking on nutrient profiles
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
            )

        time.sleep(0.1)

        # Add the first tolerable upper intake from the list of 
        # tolerable upper intakes saved in the fixtures.

        new_tolerable_upper_intake_button = self.browser.find_element_by_id(
            'id_button_new_tolerableupperintake'
        )
        new_tolerable_upper_intake_button.click()

        time.sleep(0.1)

        k = 0

        for key, value in initial_tolerable_upper_intake[k].items():
            id_from_key = 'id_' + key
            if value is not None:
                self.browser.find_element_by_id(id_from_key).send_keys(
                    str(value)
                )

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_tolerableupperintake'
        )
        save_button.click()

        time.sleep(1)

        # Test whether the saved tolerable upper intake shows up in the
        # list of tolerable upper intakes.

        xpath_ = "//*[contains(text(), " \
                 "'Dummy tolerable upper intake')]"

        tolerable_upper_intake_is_shown_in_list = check_exists_by_xpath(
            self.browser,
            xpath_,
            NoSuchElementException
        )

        self.assertTrue(tolerable_upper_intake_is_shown_in_list)

        # Test whether the saved tolerable upper intake is in the database.
        tolerable_upper_intake_query = TolerableUpperIntake.objects.filter(
            name=initial_tolerable_upper_intake[k]['name']
        )
        tolerable_upper_intake_was_saved = \
            tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_was_saved)
