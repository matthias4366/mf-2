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
# from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User
# from data.ingredients_data2 import ingredient_dict_list
# from measuredfood.models import RawIngredient2


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
            nutrient_profile_name
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

        time.sleep(10)

        # Create a FullDayOfEating with UserA called
        # "Test Full Day Of Eating made by UserA".


# Login UserB.
# Click on the menu item "Full Days Of Eating".
# Click on "Browse Full Days Of Eating".
# The UserB should be redirected to the search page.
# Enter "Test Full Day Of Eating made by UserA".
# Select Search In "Full Days Of Eating".
# Click Search.
# Test if the "Test Full Day Of Eating made by UserA" shows up in the search results.
# Click on "Test Full Day Of Eating made by UserA".
# Test if the user is redirected to the detailview of "Test Full Day Of Eating made by UserA".
# Click "Add to my Full Days Of Eating".
# Test if
# 	A) The user is redirected to their list of full days of eating.
# 	B) "Test Full Day Of Eating made by UserA" shows up in the list of Full Days Of Eating.

        self.fail('Finish the test!')
