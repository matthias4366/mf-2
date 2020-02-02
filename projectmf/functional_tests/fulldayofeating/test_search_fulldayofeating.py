from selenium.webdriver.support.ui import Select
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from ..base import FunctionalTestWithUserLoggedIn
from selenium.webdriver.common.keys import Keys
import time
# from selenium.common.exceptions import NoSuchElementException
# from functional_tests.utils.check_exists_by_xpath \
#     import check_exists_by_xpath
from measuredfood.models import (
    FullDayOfEating,
    NutrientProfile,
    SpecificNutrientTarget,
    SpecificIngredient,
    RawIngredient3,
)
# from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User
# from data.ingredients_data2 import ingredient_dict_list
from selenium.common.exceptions import NoSuchElementException


class SearchFullDayOfEatingTest(FunctionalTestWithUserLoggedIn):

    def test_search_full_day_of_eating(self):
        """
        Search functionality has been implemented with Whoosh and Haystack.
        This search functionality is tested here.
        """

        # Use the dummy user to create a full day of eating called "Full Day
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

        # Create a nutrient profile with such values that the
        # calculated_amount values will be equal to
        # list_calculated_amount_in_test.

        new_nutrient_profile_button = self.browser.find_element_by_id(
            'id_button_new_nutrient_profile'
        )
        new_nutrient_profile_button.click()

        time.sleep(0.1)

        nutrient_profile_name = 'Dummy nutrient profile'

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

        ingredient = {
            'id_ingredient_usda_api': '169738',
            'ingredient_name_usda_api':
                'Pasta, whole-wheat, dry (Includes foods '
                'for USDA\'s Food Distribution Program)',
        }

        # Simulate clicking on "Add ingredient using the FoodData Central
        # database (recommended)"
        self.browser.find_element_by_id(
            'id_button_get_from_food_data_central'
        ).click()

        self.browser.find_element_by_id(
            'id_FDC_ID'
        ).clear()

        self.browser.find_element_by_id(
            'id_FDC_ID'
        ).send_keys(
            str(ingredient['id_ingredient_usda_api'])
        )

        self.browser.find_element_by_id(
            'id_button_get_from_food_data_central'
        ).click()

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
            'Full day 1'

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

        list_rawingredient3_of_specific_ingredient = [
            ingredient['ingredient_name_usda_api']
        ]
        list_scaling_option = [
            'fixed'
        ]
        # Add specific ingredients.
        for k in range(len(list_rawingredient3_of_specific_ingredient)):
            # Choose the RawIngredient3 object for each SpecificIngredient.
            id_rawingredient3_for_specificingredient = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-rawingredient'
            select_rawingredient3 = Select(self.browser.find_element_by_id(
                id_rawingredient3_for_specificingredient
            ))
            select_rawingredient3.select_by_visible_text(
                list_rawingredient3_of_specific_ingredient[k]
            )

            # Set the scaling option of each specific ingredient to
            # 'independent'.
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
        list_nutrient_targets = [
            'Energy',
        ]
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

        # Logout user 1, i.e. dummy user.
        click_navbar_item(
            'id_menu_item_logout',
            self.browser,
            Keys,
            time,
        )

        # Register DummyUserWhoSearchesFullDayOfEating, i.e. the user who
        # will search for and copy the FullDayOfEating of DummyUser.
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
        # FullDayOfEating created by DummyUser.
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

        # Test if the FullDayOfEating shows up in the search results.
        # If it does show up, click on it.
        try:
            id_ = 'search result ' + name_dummy_full_day_of_eating
            self.browser.find_element_by_id(id_).click()
        except NoSuchElementException:
            self.fail('The full day of eating is not shown in the search '
                      'results.')

        # Test if the user is redirected to the
        # detailview of the FullDayOfEating.
        # Do that by checking whether there is a button "Copy to my full days
        # of eating". If the button is found, click it.
        try:
            self.browser.find_element_by_id(
                'id_button_copy_fulldayofeating'
            ).click()
        except NoSuchElementException:
            self.fail('The user has searched for a full day of eating and '
                      'the search result has been displayed. After clicking '
                      'on the search result, the user should be forwarded to '
                      'a DetailView of the FullDayOfEating. That DetailView '
                      'should contain a button "Copy to my full days of '
                      'eating". That button has not been found.')

        time.sleep(10)

        # Test if
        # 	A) The user is redirected to their list of full days of eating.
        # 	B) "Test Full Day Of Eating made by UserA" shows up in the list
        # 	of Full Days Of Eating.
        try:
            self.browser.find_element_by_id(
                'edit ' + name_dummy_full_day_of_eating
            ).click()
        except NoSuchElementException:
            self.fail('The user should see a list with their full days of '
                      'eating, including the full day of eating that was just '
                      'copied from another user. That is not the case.')

        # Test whether the copied FullDayOfEating is correct:
        # Test if 'Energy' is selected as a nutrient target.
        # Test if 'Whole wheat pasta' is there as a RawIngredient3.

        dummy_user_who_searches_full_day_of_eating = User.objects.filter(
            name='DummyUserWhoSearchesFullDayOfEating')

        full_day_of_eating_copy = FullDayOfEating.objects.filter(
            name=name_dummy_full_day_of_eating,
            author=dummy_user_who_searches_full_day_of_eating.id,
        )
        specific_nutrient_target_copy = SpecificNutrientTarget.objects.filter(
            fulldayofeating=full_day_of_eating_copy.id
        )
        self.assertEqual(
            specific_nutrient_target_copy.nutrient_target,
            'energy-name-1008-id',
        )

        rawingredient3_id_ = SpecificIngredient.objects.filter(
            fulldayofeating=full_day_of_eating_copy.id
        ).values('rawingredient')
        rawingredient3_id_ = list(rawingredient3_id_)
        list_name_rawingredient3_in_copy_fulldayofeating = []
        for id_k in rawingredient3_id_:
            rawingredient3_name = RawIngredient3.objects.filter(
                id=id_k
            ).values('name')
            list_name_rawingredient3_in_copy_fulldayofeating.append(
                rawingredient3_name
            )

        for predefined_rawingredient3 in \
                list_rawingredient3_of_specific_ingredient:
            self.assertIn(
                predefined_rawingredient3,
                list_name_rawingredient3_in_copy_fulldayofeating,
            )
