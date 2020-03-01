from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.base import (
    FunctionalTestWithUserLoggedIn
)
from selenium.webdriver.common.keys import Keys
import time
from measuredfood.models import (
    NutrientProfile,
    FullDayOfEating,
)
import unittest

# python manage.py test functional_tests.rawingredient3.test_rawingredient3

@unittest.skip('Duplicate renaming no longer necessary since the ID\'s '
               'are shown as well.')
class RawIngredient3Test(FunctionalTestWithUserLoggedIn):

    def test_duplicate_renaming_of_fulldayofeating_copy_fulldayofeating(self):
        """
        A user copies a FullDayOfEating object from another user. There
        already exists a FullDayOfEating object with the same name in their
        FullDayOfEating objects.

        Test if the new FullDayOfEating object gets renamed appropriately.
        "Stir fry 4540" should become "Stir fry 4541".
        """

        # User1 already exists and is called DummyUser1.

        # Create a minimal FullDayOfEating with DummyUser1, which will serve
        # as the original to be copied. (original_full_day_of_eating)

        # Use the DummyUser1 to create a full day of eating called "Full Day
        # Of Eating created by dummy user"

        # To create a FullDayOfEating it is necessary to create a a
        # NutrientProfile.
        # Simulate clicking on the navbar item for nutrient profiles.
        click_navbar_item(
            'id_menu_item_nutrient_profiles',
            self.browser,
            Keys,
            time,
        )

        time.sleep(0.1)

        new_nutrient_profile_button = self.browser.find_element_by_id(
            'id_button_new_nutrient_profile'
        )
        new_nutrient_profile_button.click()

        time.sleep(0.1)

        nutrient_profile_name = 'Nutrient profile made by DummyUser1'

        self.browser.find_element_by_id('id_name').clear()
        self.browser.find_element_by_id('id_name').send_keys(
            nutrient_profile_name
        )

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_nutrientprofile'
        )
        save_button.click()

        time.sleep(1)

        # Test whether the saved nutrient profile is in the database.
        nutrient_profile_query = NutrientProfile.objects.filter(
            name=nutrient_profile_name
        )
        nutrient_profile_was_saved = nutrient_profile_query.exists()
        self.assertTrue(nutrient_profile_was_saved)

        # To create a FullDayOfEating object, it is also necessary to create
        # some RawIngredient3 objects.

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
        )

        # It will have an ingredient that will be the focal point of the
        # test: original_name = 'Pasta 4540'.
        original_name = 'Pasta 4540'
        expected_duplicate_name = 'Pasta 4541'

        # Add a placeholder ingredient manually.
        # The code says 'ingredient_name_usda_api' because it is copy pasted
        # to save development time.
        ingredient_dict_list = [
            {
                'id_ingredient_usda_api': None,
                'ingredient_name_usda_api':
                    original_name,
            },
        ]

        list_rawingredient3_of_specific_ingredient = []
        for ingredient_dict_k in ingredient_dict_list:
            list_rawingredient3_of_specific_ingredient.append(
                ingredient_dict_k['ingredient_name_usda_api']
            )

        # Make the original ingredient.
        for ingredient_dict_k in ingredient_dict_list:
            self.browser.find_element_by_id(
                'id_button_new_rawingredient3'
            ).click()
            self.browser.find_element_by_id('id_name').send_keys(
                ingredient_dict_k['ingredient_name_usda_api']
            )
            self.browser.find_element_by_id(
                'id_button_save_new_rawingredient3').click()

        # Create FullDayOfEating object.

        # Simulate clicking the navbar item Full days of eating.
        click_navbar_item(
            'id_menu_item_fulldayofeating',
            self.browser,
            Keys,
            time,
        )
        time.sleep(0.1)

        # Simulate click on 'New full day of eating' button.

        new_fulldayofeating_button = self.browser.find_element_by_id(
            'id_button_new_fulldayofeating'
        )
        new_fulldayofeating_button.click()

        name_dummy_full_day_of_eating = \
            'Original Full day'

        # Type in the name of the new full day of eating.
        self.browser.find_element_by_id('id_name').send_keys(
            name_dummy_full_day_of_eating
        )

        # From the nutrient profile dropdown menu, select the nutrient
        # profile that was created at the beginning of this test.

        select_nutrient_profile = Select(self.browser.find_element_by_id(
            'id_nutrient_profile'
        ))
        select_nutrient_profile.select_by_visible_text(
            nutrient_profile_name
        )

        save_full_day_of_eating_button = self.browser.find_element_by_id(
            'id_button_save_new_fulldayofeating'
        )
        save_full_day_of_eating_button.click()

        list_scaling_option = [
            'fixed',
        ]

        # Add specific ingredients.
        for k in range(len(ingredient_dict_list)):
            # Choose the RawIngredient3 object for each SpecificIngredient.
            id_rawingredient3_for_specificingredient = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-rawingredient'
            select_rawingredient3 = Select(self.browser.find_element_by_id(
                id_rawingredient3_for_specificingredient
            ))
            select_rawingredient3.select_by_visible_text(
                ingredient_dict_list[k]['ingredient_name_usda_api']
            )

            # Set the scaling option of each specific ingredient.
            id_scaling_option = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-scaling_option'
            select_scaling_option = Select(self.browser.find_element_by_id(
                id_scaling_option
            ))
            select_scaling_option.select_by_visible_text(
                list_scaling_option[k]
            )

            # The default amount of 100 g works out fine for this test,
            # hence no base amounts are entered.

            # Simulate clicking the save button
            save_changes_button = self.browser.find_element_by_id(
                'save_changes_formset_fulldayofeating'
            )
            save_changes_button.click()
            time.sleep(0.5)

        # Set some nutrient targets to see if they get copied properly as well.
        # List of nutrient targets as they are displayed to the user.
        list_nutrient_targets = [
            'Energy',
        ]
        # # List of nutrient targets as they are called internally in the
        # # application.
        # list_preset_nutrient_targets = [
        #     'energy-name-1008-id'
        # ]
        # Add nutrient targets.
        for k in range(len(list_nutrient_targets)):
            id_k = \
                'id_specificnutrienttarget_set-' \
                + str(k) \
                + '-nutrient_target'

            select_nutrient_target = Select(self.browser.find_element_by_id(
                id_k
            ))
            select_nutrient_target.select_by_visible_text(
                list_nutrient_targets[k]
            )
            # Simulate clicking the save button
            save_changes_button = self.browser.find_element_by_id(
                'save_changes_formset_fulldayofeating'
            )
            save_changes_button.click()
            time.sleep(0.5)

        # Check that full day of eating object exists in the database.
        full_day_of_eating_query = FullDayOfEating.objects.filter(
            name=name_dummy_full_day_of_eating
        )
        full_day_of_eating_was_saved = full_day_of_eating_query.exists()
        self.assertTrue(full_day_of_eating_was_saved)

        # Logout DummyUser1.
        click_navbar_item(
            'id_menu_item_logout',
            self.browser,
            Keys,
            time,
        )

        # Register DummyUserWhoSearchesFullDayOfEating, i.e. the user who
        # will search for and copy the FullDayOfEating of DummyUser1.
        click_navbar_item(
            'id_menu_item_register',
            self.browser,
            Keys,
            time,
        )

        # Create a new dummy user.
        dummy_username = 'DummyUserWhoSearchesFullDayOfEating'
        dummy_email = 'DummyUserWhoSearchesFullDayOfEating@gmail.com'
        dummy_password = 'testpassword'

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

        time.sleep(0.5)

        # Check if the dummy user object exists in the database.
        self.user = User.objects.filter(
            username=dummy_username,
        )

        dummy_user_exists = self.user.exists()

        self.assertTrue(dummy_user_exists)

        # Find login elements
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')

        # Input values into the fields
        username_field.send_keys(dummy_username)
        password_field.send_keys(dummy_password)

        # Simulate clicking on Log In
        click_navbar_item(
            'id_button_login',
            self.browser,
            Keys,
            time,
        )

        # DummyUserWhoSearchesFullDayOfEating create the same RawIngredient3 as
        # DummyUser1.

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
        )

        # Create the same RawIngredient3 as DummyUser1.
        for ingredient_dict_k in ingredient_dict_list:
            self.browser.find_element_by_id(
                'id_button_new_rawingredient3'
            ).click()
            self.browser.find_element_by_id('id_name').send_keys(
                ingredient_dict_k['ingredient_name_usda_api']
            )
            self.browser.find_element_by_id(
                'id_button_save_new_rawingredient3').click()

        click_navbar_item(
            'id_menu_item_fulldayofeating',
            self.browser,
            Keys,
            time,
        )

        browse_fulldayofeating_button = self.browser.find_element_by_id(
            'id_button_browse_fulldayofeating'
        )
        browse_fulldayofeating_button.click()

        # The DummyUserWhoSearchesFullDayOfEating should be redirected to
        # the search page.

        # The DummyUserWhoSearchesFullDayOfEating searches for the
        # FullDayOfEating created by DummyUser1.
        self.browser.find_element_by_id('id_q').clear()
        self.browser.find_element_by_id('id_q').send_keys(
            name_dummy_full_day_of_eating
        )

        # Select Search In "Full Days Of Eating".
        # TODO: Customize the search.html file to get a more informative id
        #  than id_models_0.
        self.browser.find_element_by_id('id_models_0').click()
        time.sleep(0.1)

        # Click Search.
        self.browser.find_element_by_id('id_search').click()

        time.sleep(0.1)

        # Test if the FullDayOfEating shows up in the search results.
        # If it does show up, click on it.
        id_ = 'search result ' + name_dummy_full_day_of_eating
        self.browser.find_element_by_id(id_).click()

        # Test if the user is redirected to the
        # detailview of the FullDayOfEating.
        # Do that by checking whether there is a button "Copy to my full days
        # of eating". If the button is found, click it.
        self.browser.find_element_by_id(
            'id_button_copy_fulldayofeating'
        ).click()

        time.sleep(0.1)

        # Test if
        # 	A) The user is redirected to their list of full days of eating.
        # 	B) "Test Full Day Of Eating made by UserA" shows up in the list
        # 	of Full Days Of Eating.
        # If the FullDayOfEating has not been copied, the edit button is not
        # found and the test crashes and throws an error.
        edit_button = self.browser.find_element_by_id(
            'edit ' + name_dummy_full_day_of_eating
        )
        edit_button.click()

        # Go into the RawIngredient3 objects of DummyUser2. There should be
        # exactly one named 'Pasta 4540' and exactly one named 'Pasta 4541'.

        # Simulate clicking on the menu item "Ingredients".
        click_navbar_item(
            'id_menu_item_rawingredients3',
            self.browser,
            Keys,
            time,
        )

        ingredients_with_original_name = self.browser.find_elements_by_id(
            'edit ' + original_name
        )
        n_ingredients_with_original_name = len(ingredients_with_original_name)
        self.assertEqual(n_ingredients_with_original_name, 1)

        ingredients_with_name_of_duplicate = self.browser.find_elements_by_id(
            'edit ' + expected_duplicate_name
        )
        n_ingredients_with_name_of_duplicate = len(
            ingredients_with_name_of_duplicate
        )
        self.assertEqual(n_ingredients_with_name_of_duplicate, 1)

        self.fail('Finish the test!')
