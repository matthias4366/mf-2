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
)
from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User

# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')


class FullDayOfEatingTest(FunctionalTestWithUserLoggedIn):
    
    def test_calculate_full_day_of_eating_of_other_user(self):
        """
        Through url forgery, a user could attempt the calculate the full day 
        of eating of another user. That is thwarted with the check_if_author 
        function. The test is passed if the attempt to calculate the foreign 
        full day of eating is denied.
        """
        # Create another user.
        foreign_user = User.objects.create(
            username='Other User'
        )
        
        # Create a full day of eating for the foreign user. Start with the 
        # nutrient profile.
        foreign_nutrientprofile = NutrientProfile.objects.create(
            name='Nutrient profile from other user',
            author=foreign_user
        )
        
        foreign_full_day_of_eating = FullDayOfEating.objects.create(
            name='Full day of eating from foreign user',
            author=foreign_user,
            nutrient_profile=foreign_nutrientprofile,
        )

        url_foreign_full_day_of_eating = \
            self.live_server_url \
            + '/fulldayofeating/'\
            + str(foreign_full_day_of_eating.id)\
            + '/calculate/'

        # Try opening the edit page of the foreign FullDayOfEating object.
        self.browser.get(url_foreign_full_day_of_eating)

        # Test whether the appropriate error page is shown.
        error_paragraph = self.browser.find_elements_by_id(
            'UserIsNotAuthorError'
        )
        error_page_is_shown = \
            len(error_paragraph) > 0
        self.assertTrue(error_page_is_shown)

    def test_calculate_full_day_of_eating_without_ingredient(self):
        """
        The test case is the creation of a full day of eating without a
        SpecificIngredient. It is successful if the correct error message is
        produced.
        """

        # The user objects can be accessed with self.user.

        # Create a NutrientProfile.
        # Simulate clicking on the navbar item for nutrient profiles.
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

        # Iterator for the nutrient profile.
        k_np = 0

        for key, value in nutrient_profile_dict_list[k_np].items():
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

        # Test whether the saved nutrient profile is in the database.
        nutrient_profile_query = NutrientProfile.objects.filter(
            name=nutrient_profile_dict_list[k_np]['name']
        )
        nutrient_profile_was_saved = nutrient_profile_query.exists()
        self.assertTrue(nutrient_profile_was_saved)

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

        name_dummy_full_day_of_eating = 'Dummy full day of eating'

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
            nutrient_profile_dict_list[k_np]['name']
        )

        save_full_day_of_eating_button = self.browser.find_element_by_id(
            'id_button_save_new_fulldayofeating'
        )
        save_full_day_of_eating_button.click()

        # Check that full day of eating object exists in the database.
        full_day_of_eating_query = FullDayOfEating.objects.filter(
            name=name_dummy_full_day_of_eating
        )
        full_day_of_eating_was_saved = full_day_of_eating_query.exists()
        self.assertTrue(full_day_of_eating_was_saved)

        time.sleep(5)

        # The user is redirected to the list of full days of eating.
        # Find the correct full day of eating and click the edit button.
        edit_button = self.browser.find_element_by_id(
            'edit '+name_dummy_full_day_of_eating
        )
        edit_button.click()

        # Click the button 'Calculate full day of eating'.
        calculate_button = self.browser.find_element_by_id(
            'id_button_calculate_full_day_of_eating'
        )
        calculate_button.click()

        # time.sleep(7)

        # Check if the correct error message is displayed.
        # id = NoSpecificIngredientInFullDayOfEatingError

        # Test whether the appropriate error page is shown.
        error_paragraph = self.browser.find_elements_by_id(
            'NoSpecificIngredientInFullDayOfEatingError'
        )
        error_page_is_shown = \
            len(error_paragraph) > 0
        self.assertTrue(error_page_is_shown)
