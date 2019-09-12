from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from data.ingredients_data2 import ingredient_dict_list
from .base import (
    # FunctionalTest,
    FunctionalTestWithUserLoggedIn)
from selenium.webdriver.common.keys import Keys
import time
from measuredfood.models import RawIngredient2
from django.contrib.auth.models import User
# from django.test import Client
# from django.urls import reverse
# from selenium.webdriver.common.by import By


# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class RawIngredient2Test(FunctionalTestWithUserLoggedIn):

    def test_rawingredient2_creation(self):

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
            )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public':
                if value is not None:
                    self.browser. \
                        find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

    def test_rawingredient2_creation_invalid_input(self):
        """
        When filling out the creation form for the RawIngredient2, the "name"
        field is necessary. It is tested that the user can not add a new
        RawIngredient2 without a "name".
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            # The name is left blank on purpose, which is expected to
            # impede the creation of a RawIngredient2 instance.
            if key != 'is_public' and key != 'name':
                if value is not None:
                    self.browser. \
                        find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertFalse(rawingredient2_was_saved)

    def test_rawingredient2_edit_save_changes(self):
        """
        A RawIngredient2 is created. The created RawIngredient2 is edited
        and the changes are saved. It is tested whether the RawIngredient2
        instance in the database reflects the edit.
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public' and value is not None:
                self.browser.find_element_by_name(key).clear()
                self.browser.find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

        # Test that after saving the ingredient the user has been redirected
        # to the list of RawIngredient2 objects.
        self.assertIn('rawingredient2/list/', self.browser.current_url)

        # Find the correct edit button by its id.
        edit_button = self.browser.find_element_by_id(
            'edit '+ingredient_dict_list[k]['name']
        )

        edit_button.click()

        # Test if the user is redirected to the update page of the
        # RawIngredient2 instance.
        self.assertIn('update', self.browser.current_url)

        # Make some changes.
        changed_name = ingredient_dict_list[k]['name'] + ' CHANGED'
        # Delete old name.
        self.browser.find_element_by_name('name').clear()
        # Type in new name.
        self.browser.find_element_by_name('name').send_keys(changed_name)

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the changed RawIngredient2 instance is found in the database.
        changed_rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=changed_name
        )
        changed_rawingredient2_was_saved = \
            changed_rawingredient2_saved_object.exists()
        self.assertTrue(changed_rawingredient2_was_saved)

        # Check if the changed RawIngredient2 instance is found in the list of
        # RawIngredient2 objects.
        changed_rawingredient2_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph '+changed_name
            )

        changed_rawingredient2_is_shown_in_list = \
            len(changed_rawingredient2_paragraph) > 0

        self.assertTrue(changed_rawingredient2_is_shown_in_list)

    def test_rawingredient2_edit_discard_changes(self):
        """
        A RawIngredient2 is created. The created RawIngredient2 is edited
        and the changes are not saved. It is tested whether the RawIngredient2
        instance in the database remains unchanged.
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public' and value is not None:
                self.browser.find_element_by_name(key).clear()
                self.browser.find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

        # Test that after saving the ingredient the user has been redirected
        # to the list of RawIngredient2 objects.
        self.assertIn('rawingredient2/list/', self.browser.current_url)

        # Find the correct edit button by its id.
        edit_button = self.browser.find_element_by_id(
            'edit '+ingredient_dict_list[k]['name']
        )

        edit_button.click()

        # Test if the user is redirected to the update page of the
        # RawIngredient2 instance.
        self.assertIn('update', self.browser.current_url)

        # Make some changes.
        changed_name = ingredient_dict_list[k]['name'] + ' CHANGED'
        # Delete old name.
        self.browser.find_element_by_name('name').clear()
        # Type in new name.
        self.browser.find_element_by_name('name').send_keys(changed_name)

        # Simulate clicking the cancel button.
        cancel_button = self.browser.find_element_by_id(
            'button_cancel_save_changes_rawingredient2'
        )
        cancel_button.click()

        # Test whether the RawIngredient2 object is unafflicted by changes by
        # two ways.
        # The first way is to test whether the RawIngredient2 object can be
        # found in the database using the unchanged name.

        unchanged_rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_is_unchanged_in_database = \
            unchanged_rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_is_unchanged_in_database)

        # The second way is to test whether the RawIngredient2 object can be
        # found in the list using the unchanged name.

        unchanged_rawingredient2_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph '+ingredient_dict_list[k]['name']
            )

        rawingredient2_is_shown_in_list_unchanged = \
            len(unchanged_rawingredient2_paragraph) > 0

        self.assertTrue(rawingredient2_is_shown_in_list_unchanged)

    def test_rawingredient2_delete_confirm_delete(self):
        """
        A RawIngredient2 object is created. The test case consists of the
        clicking of 'Delete' and the subsequent confirming by clicking 'Yes,
        Delete'. It is tested whether the RawIngredient2 object has been
        successfully removed from the database and the list of RawIngredient2
        objects.
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public' and value is not None:
                self.browser.find_element_by_name(key).clear()
                self.browser.find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

        # Test that after saving the ingredient the user has been redirected
        # to the list of RawIngredient2 objects.
        self.assertIn('rawingredient2/list/', self.browser.current_url)

        # Find the correct delete button by its id.

        delete_button = self.browser.find_element_by_id(
            'delete '+ingredient_dict_list[k]['name']
        )
        delete_button.click()

        # Test if the user is redirected to the delete page of the
        # RawIngredient2 instance.
        self.assertIn('delete', self.browser.current_url)

        confirm_delete_button = self.browser.find_element_by_id(
            'confirm_delete'
        )
        confirm_delete_button.click()

        # Test whether the RawIngredient2 object has been deleted in two ways.

        # The first way is to test whether the RawIngredient2 object can
        # be found in the database.

        rawingredient2_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_is_in_database = \
            rawingredient2_object.exists()
        self.assertFalse(rawingredient2_is_in_database)

        # The second way is to test whether the RawIngredient2 object can
        # be found in the list using the unchanged name.

        rawingredient2_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph '+ingredient_dict_list[k]['name']
            )

        rawingredient2_is_shown_in_list = \
            len(rawingredient2_paragraph) > 0

        self.assertFalse(rawingredient2_is_shown_in_list)

    def test_rawingredient2_delete_cancel_delete(self):
        """
        A RawIngredient2 object is created. The test case consists of the
        clicking of 'Delete' and the subsequent cancelling by clicking
        'Cancel'. It is tested whether the RawIngredient2 object still
        exists in the database and in the list of RawIngredient2 objects.
        """

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add the first ingredient from the list.
        k = 0

        new_ingredient_button = self.browser.find_element_by_id(
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(1)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public' and value is not None:
                self.browser.find_element_by_name(key).clear()
                self.browser.find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button.
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

        # Check if the RawIngredient2 instance is found in the database.
        rawingredient2_saved_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_was_saved = rawingredient2_saved_object.exists()
        self.assertTrue(rawingredient2_was_saved)

        # Test that after saving the ingredient the user has been redirected
        # to the list of RawIngredient2 objects.
        self.assertIn('rawingredient2/list/', self.browser.current_url)

        # Find the correct delete button by its id.

        delete_button = self.browser.find_element_by_id(
            'delete '+ingredient_dict_list[k]['name']
        )
        delete_button.click()

        # Test if the user is redirected to the delete page of the
        # RawIngredient2 instance.
        self.assertIn('delete', self.browser.current_url)

        cancel_delete_button = self.browser.find_element_by_id(
            'cancel_delete'
        )
        cancel_delete_button.click()

        # Test whether the RawIngredient2 object has been deleted in two ways.

        # The first way is to test whether the RawIngredient2 object can
        # be found in the database.

        rawingredient2_object = RawIngredient2.objects.filter(
            name=ingredient_dict_list[k]['name']
        )
        rawingredient2_is_in_database = \
            rawingredient2_object.exists()
        self.assertTrue(rawingredient2_is_in_database)

        # The second way is to test whether the RawIngredient2 object can
        # be found in the list using the unchanged name.

        rawingredient2_paragraph = \
            self.browser.find_elements_by_id(
                'paragraph '+ingredient_dict_list[k]['name']
            )

        rawingredient2_is_shown_in_list = \
            len(rawingredient2_paragraph) > 0

        self.assertTrue(rawingredient2_is_shown_in_list)

    def test_user_can_not_edit_rawingredient2_of_other_user(self):
        """
        It should not be possible for users to edit any object from another
        user. Here, it is tested whether the user can edit other users
        RawIngredient2 objects. If a user were to know (or guess) the id of a
        foreign object, it is possible in principle to access that
        object via url forgery.
        """

        other_user = User.objects.create(
            username='Other User'
        )

        # Create a RawIngredient2 object that belong to a different user.
        foreign_rawingredient2 = RawIngredient2.objects.create(
            name='Ingredient from other user',
            author=other_user,
        )

        url_foreign_rawingredient2 = \
            self.live_server_url \
            + '/rawingredient2/' \
            + str(foreign_rawingredient2.id) \
            + '/update/'

        # Try opening the edit page of the different RawIngredient2.
        self.browser.get(url_foreign_rawingredient2)

        # Test whether the appropriate error page is shown.
        error_paragraph = self.browser.find_elements_by_id(
            'error_message_not_your_rawingredient2_to_edit'
        )
        error_page_is_shown = \
            len(error_paragraph) > 0
        self.assertTrue(error_page_is_shown)

    def test_user_can_not_delete_rawingredient2_of_other_user(self):
        """
        It should not be possible for users to delete any object from another
        user. Here, it is tested whether the user can delete other users
        RawIngredient2 objects via url forgery.
        """

        other_user = User.objects.create(
            username='Other User'
        )

        # Create a RawIngredient2 object that belong to a different user.
        foreign_rawingredient2 = RawIngredient2.objects.create(
            name='Ingredient from other user',
            author=other_user,
        )

        # Forge the url to try to delete the other users RawIngredient2.
        url_foreign_rawingredient2 = \
            self.live_server_url \
            + '/rawingredient2/' \
            + str(foreign_rawingredient2.id) \
            + '/delete/'

        self.browser.get(url_foreign_rawingredient2)

        error_message_element = self.browser.find_element_by_xpath(
            "/html/body/h1")

        error_message = error_message_element.text

        self.assertEqual(error_message, '403 Forbidden')
