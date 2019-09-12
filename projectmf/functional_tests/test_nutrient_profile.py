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

    def test_nutrient_profile_creation_with_invalid_data(self):
        """
        Test the creation of a nutrient profile with invalid data, i.e. other
        fields are filled out but the name is left blank.
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
            # Leave the name field blank to simulate a case of trying to
            # create a NutrientProfile without filling out all the required
            # fields.
            if key != 'name':
                id_from_key = 'id_' + key
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

        # This test is not necessary. The other test is sufficient. If the
        # NutrientProfile object is not in the database, it is impossible for
        # it to show up in the list.
        # (Test whether the saved nutrient profile shows up in the list of
        # nutrient profiles.)

        # Test whether the saved nutrient profile is in the database.
        nutrient_profile_query = NutrientProfile.objects.filter(
            name=nutrient_profile_dict_list[k]['name']
        )
        nutrient_profile_was_saved = nutrient_profile_query.exists()
        self.assertFalse(nutrient_profile_was_saved)

    def test_nutrientprofile_edit_save_changes(self):
        """
        A NutrientProfile is created. The NutrientProfile is edited and the
        changes are saved. It is tested whether the NutrientProfile instance
        in the database reflects the edit.
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

        # Now that the nutrient profile has been saved, it is edited.

        # Simulate clicking on nutrient profiles
        click_navbar_item(
            'id_menu_item_nutrient_profiles',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        edit_button = self.browser.find_element_by_id(
            'edit '+nutrient_profile_dict_list[k]['name']
        )
        edit_button.click()

        # Test if the user is redirected to the update page of the nutrient
        # profile.
        self.assertIn('update', self.browser.current_url)
        self.assertIn('nutrientprofile', self.browser.current_url)

        # Make some changes
        changed_name = nutrient_profile_dict_list[k]['name'] + ' CHANGED'
        # Delete old name.
        self.browser.find_element_by_name('name').clear()
        # Type in new name.
        self.browser.find_element_by_name('name').send_keys(changed_name)

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_nutrientprofile'
        )
        save_button.click()

        # Check if the changed NutrientProfile object is found in the database.
        changed_nutrientprofile = NutrientProfile.objects.filter(
            name=changed_name
        )
        changed_nutrientprofile_was_saved = \
            changed_nutrientprofile.exists()
        self.assertTrue(changed_nutrientprofile_was_saved)

        # Check if the changed NutrientProfile object is found in the list of
        # NutrientProfile objects.
        changed_nutrientprofile_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph '+changed_name
            )

        changed_nutrientprofile_is_shown_in_list = \
            len(changed_nutrientprofile_paragraph) > 0

        self.assertTrue(changed_nutrientprofile_is_shown_in_list)
