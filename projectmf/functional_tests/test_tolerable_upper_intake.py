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
        # Simulate clicking on tolerable upper intakes
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

    def test_tolerable_upper_intake_creation_with_invalid_data(self):
        """
        Test of the creation of a TolerableUpperIntake object where the input
        data is not valid, i.e. the name is missing. The test is successfull if
        the TolerableUpperIntake object is not saved to the database.
        """

        # Simulate the clicking on the tolerable upper intakes navbar item.
        # Simulate clicking on tolerable upper intakes
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
            # Skip the name, making the input invalid as the name is necessary.
            if key != 'name':
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

        # Test whether the saved tolerable upper intake is in the database.
        tolerable_upper_intake_query = TolerableUpperIntake.objects.filter(
            name=initial_tolerable_upper_intake[k]['name']
        )
        tolerable_upper_intake_was_saved = \
            tolerable_upper_intake_query.exists()
        self.assertFalse(tolerable_upper_intake_was_saved)

    def test_tolerable_upper_intake_edit_save_changes(self):
        """
        A TolerableUpperIntake is created. The TolerableUpperIntake is edited 
        and the changes are saved. It is tested whether the TolerableUpperIntake 
        instance in the database reflects the edit.
        """

        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        # Add the first tolerable upper intake from the list of tolerable upper 
        # intakes saved in the fixtures.

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

        # Test whether the saved tolerable upper intake shows up in the list of
        # tolerable upper intakes.

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
        tolerable_upper_intake_was_saved = tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_was_saved)

        # Now that the tolerable upper intake has been saved, it is edited.

        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        edit_button = self.browser.find_element_by_id(
            'edit ' + initial_tolerable_upper_intake[k]['name']
        )
        edit_button.click()

        # Test if the user is redirected to the update page of the tolerable
        # upper intake.
        self.assertIn('update', self.browser.current_url)
        self.assertIn('tolerableupperintake', self.browser.current_url)

        # Make some changes
        changed_name = initial_tolerable_upper_intake[k]['name'] + ' CHANGED'
        # Delete old name.
        self.browser.find_element_by_name('name').clear()
        # Type in new name.
        self.browser.find_element_by_name('name').send_keys(changed_name)

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_tolerableupperintake'
        )
        save_button.click()

        # Check if the changed TolerableUpperIntake object is found in the
        # database.
        changed_tolerable_upper_intake = TolerableUpperIntake.objects.filter(
            name=changed_name
        )
        changed_tolerable_upper_intake_was_saved = \
            changed_tolerable_upper_intake.exists()
        self.assertTrue(changed_tolerable_upper_intake_was_saved)

        # Check if the changed TolerableUpperIntake object is found in the list
        # of TolerableUpperIntake objects.
        changed_tolerable_upper_intake_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph ' + changed_name
            )

        changed_tolerable_upper_intake_is_shown_in_list = \
            len(changed_tolerable_upper_intake_paragraph) > 0

        self.assertTrue(changed_tolerable_upper_intake_is_shown_in_list)

    def test_tolerable_upper_intake_edit_discard_changes(self):
        """
        A TolerableUpperIntake is created. The TolerableUpperIntake is edited
        and the changes are not saved. It is tested whether the
        TolerableUpperIntake instance in the database is still the same as
        before.
        """

        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        # Add the first tolerable upper intake from the list of tolerable 
        # upper intakes saved in the fixtures.

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

        # Test whether the saved tolerable upper intake shows up in the list of
        # tolerable upper intakes.

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
        tolerable_upper_intake_was_saved = tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_was_saved)

        # Now that the tolerable upper intake has been saved, it is edited.

        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        edit_button = self.browser.find_element_by_id(
            'edit ' + initial_tolerable_upper_intake[k]['name']
        )
        edit_button.click()

        # Test if the user is redirected to the update page of the tolerable 
        # upper intakes.
        self.assertIn('update', self.browser.current_url)
        self.assertIn('tolerableupperintake', self.browser.current_url)

        # Make some changes
        changed_name = initial_tolerable_upper_intake[k]['name'] + ' CHANGED'
        # Delete old name.
        self.browser.find_element_by_name('name').clear()
        # Type in new name.
        self.browser.find_element_by_name('name').send_keys(changed_name)

        # Simulate clicking the cancel button
        cancel_button = self.browser.find_element_by_id(
            'cancel_save_tolerable_upper_intake'
        )
        cancel_button.click()

        # Check whether the TolerableUpperIntake object in the database is still
        # unchanged.
        tolerable_upper_intake_query = TolerableUpperIntake.objects.filter(
            name=initial_tolerable_upper_intake[k]['name']
        )
        tolerable_upper_intake_unchanged = \
            tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_unchanged)

        # Check if the TolerableUpperIntake object in the list of
        # TolerableUpperIntake objects remains unchanged.

        unchanged_tolerable_upper_intake_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph ' + initial_tolerable_upper_intake[k]['name']
            )
        unchanged_tolerable_upper_intake_is_shown_in_list = \
            len(unchanged_tolerable_upper_intake_paragraph) > 0

        self.assertTrue(unchanged_tolerable_upper_intake_is_shown_in_list)

    def test_tolerable_upper_intake_delete_confirm_delete(self):
        """
        A TolerableUpperIntake object is created. The test case consists of
        clicking on 'Delete' and the subsequent confirming by clicking on
        'Yes, Delete'. It is tested whether the TolerableUpperIntake object has
        been removed from the database and from the list of TolerableUpperIntake
        objects.
        """
        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        # Add the first tolerable upper intake from the list of tolerable upper
        # intakes saved in the fixtures.

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

        # Test whether the saved tolerable upper intake shows up in the list of
        # tolerable upper intakes.

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
        tolerable_upper_intake_was_saved = tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_was_saved)

        # Now that the TolerableUpperIntake object has been created, it is
        # deleted.

        # Find the correct delete button by its id.
        delete_button = self.browser.find_element_by_id(
            'delete ' + initial_tolerable_upper_intake[k]['name']
        )
        delete_button.click()

        # Test whether the user is redirected to the delete page of
        # TolerableUpperIntake instance.
        self.assertIn('delete', self.browser.current_url)
        self.assertIn('tolerableupperintake', self.browser.current_url)

        confirm_delete_button = self.browser.find_element_by_id(
            'confirm_delete'
        )
        confirm_delete_button.click()

        # Test whether the TolerableUpperIntake object has been deleted in two
        # ways.

        # The first way is to test whether the TolerableUpperIntake object can
        # be found in the database.

        tolerable_upper_intake_query = TolerableUpperIntake.objects.filter(
            name=initial_tolerable_upper_intake[k]['name']
        )
        tolerable_upper_intake_is_in_database = \
            tolerable_upper_intake_query.exists()
        self.assertFalse(tolerable_upper_intake_is_in_database)

        # The second way is to test whether the TolerableUpperIntake object can
        # be found in the list using the unchanged name.

        tolerable_upper_intake_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph ' + initial_tolerable_upper_intake[k]['name']
            )

        tolerable_upper_intake_is_shown_in_list = \
            len(tolerable_upper_intake_paragraph) > 0

        self.assertFalse(tolerable_upper_intake_is_shown_in_list)

    def test_tolerable_upper_intake_delete_cancel_delete(self):
        """
        A TolerableUpperIntake object is created. The test case consists of
        clicking on 'Delete' and the subsequent cancelling by clicking on
        'Cancel'. It is tested whether the TolerableUpperIntake object remains
        in the database and in the list of TolerableUpperIntake objects.
        """
        # Simulate clicking on tolerable upper intakes
        click_navbar_item(
            'id_menu_item_tolerableupperintake',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        # Add the first tolerable upper intake from the list of tolerable upper
        # intakes saved in the fixtures.

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

        # Test whether the saved tolerable upper intake shows up in the list of
        # tolerable upper intakes.

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
        tolerable_upper_intake_was_saved = tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_was_saved)

        # Now that the TolerableUpperIntake object has been created, it is
        # deleted.

        # Find the correct delete button by its id.
        delete_button = self.browser.find_element_by_id(
            'delete ' + initial_tolerable_upper_intake[k]['name']
        )
        delete_button.click()

        # Test whether the user is redirected to the delete page of
        # TolerableUpperIntake instance.
        self.assertIn('delete', self.browser.current_url)
        self.assertIn('tolerableupperintake', self.browser.current_url)

        cancel_delete_button = self.browser.find_element_by_id(
            'cancel_delete'
        )
        cancel_delete_button.click()

        # Test whether the TolerableUpperIntake object has been deleted in two
        # ways.

        # The first way is to test whether the TolerableUpperIntake object can
        # be found in the database.

        tolerable_upper_intake_query = TolerableUpperIntake.objects.filter(
            name=initial_tolerable_upper_intake[k]['name']
        )
        tolerable_upper_intake_is_in_database = \
            tolerable_upper_intake_query.exists()
        self.assertTrue(tolerable_upper_intake_is_in_database)

        # The second way is to test whether the TolerableUpperIntake object can
        # be found in the list using the unchanged name.

        tolerable_upper_intake_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph ' + initial_tolerable_upper_intake[k]['name']
            )

        tolerable_upper_intake_is_shown_in_list = \
            len(tolerable_upper_intake_paragraph) > 0

        self.assertTrue(tolerable_upper_intake_is_shown_in_list)

    # def test_user_can_not_edit_TolerableUpperIntake_of_other_user(self):
    #     """
    #     Url forgery used to access the tolerable upper intakes of other users has
    #     to be prevented. It is tested whether the attempt to edit the
    #     tolerable upper intake of another user is successfully thwarted.
    #     """
    # 
    #     other_user = User.objects.create(
    #         username='Other User'
    #     )
    # 
    #     foreign_TolerableUpperIntake = TolerableUpperIntake.objects.create(
    #         name='tolerable upper intake from other user',
    #         author=other_user
    #     )
    # 
    #     url_foreign_TolerableUpperIntake = \
    #         self.live_server_url \
    #         + '/TolerableUpperIntake/' \
    #         + str(foreign_TolerableUpperIntake.id) \
    #         + '/update/'
    # 
    #     # Try opening the edit page of the foreign TolerableUpperIntake object.
    #     self.browser.get(url_foreign_TolerableUpperIntake)
    # 
    #     # Test whether the appropriate error page is shown.
    #     error_paragraph = self.browser.find_elements_by_id(
    #         'error_message_url_forgery'
    #     )
    #     error_page_is_shown = \
    #         len(error_paragraph) > 0
    #     self.assertTrue(error_page_is_shown)
    # 
    # def test_user_can_not_delete_TolerableUpperIntake_of_other_user(self):
    #     """
    #     It should not be possible for users to delete any object from another
    #     user. Here, it is tested whether the user can delete other users
    #     TolerableUpperIntake objects via url forgery.
    #     """
    # 
    #     other_user = User.objects.create(
    #         username='Other User'
    #     )
    # 
    #     # Create a TolerableUpperIntake object that belong to a different user.
    #     foreign_TolerableUpperIntake = TolerableUpperIntake.objects.create(
    #         name='tolerable upper intake from other user',
    #         author=other_user,
    #     )
    # 
    #     # Forge the url to try to delete the other users TolerableUpperIntake.
    #     url_foreign_TolerableUpperIntake = \
    #         self.live_server_url \
    #         + '/TolerableUpperIntake/' \
    #         + str(foreign_TolerableUpperIntake.id) \
    #         + '/delete/'
    # 
    #     self.browser.get(url_foreign_TolerableUpperIntake)
    # 
    #     error_message_element = self.browser.find_element_by_xpath(
    #         "/html/body/h1")
    # 
    #     error_message = error_message_element.text
    # 
    #     self.assertEqual(error_message, '403 Forbidden')
