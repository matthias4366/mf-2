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
# from django.contrib.auth.models import User
from data.ingredients_data2 import ingredient_dict_list
from measuredfood.models import RawIngredient2

# import the ingredient dictionaries
import sys

sys.path.insert(0, '/projectmf/data/')


class FullDayOfEatingTest(FunctionalTestWithUserLoggedIn):

    def test_no_value_for_targeted_nutrient_error(self):
        """
        In the full day of eating, a multitude of nutrient goals are given in
        the NutrientProfile. Only a part of these nutrients is targeted for the
        calculation. The nutrients which are targeted must have a value in
        the NutrientProfile. The test case is to create a full day of eating
        with a NutrientProfile with missing values to test whether the
        correct error message is displayed. The error that should be raised
        is NoValueForTargetedNutrientError.

        Implementation:

        Target 3 nutrients but only have a value for 1 of the nutrients in
        the nutrient profile. This ensures
        1) that the error message displays a list of multiple nutrients
        whose values are missing and
        2) that there are no false positives, as the nutrient for which
        there is a value should not be displayed in the error message as a
        nutrient with a missing value in the nutrient profile.

        Target calories, protein and calcium and only provide a value for
        calcium.

        Ingredients: white rice, protein powder, calcium citrate.

        Add all the ingredients from the fixtures to the user's collection
        of ingredients.

        To choose the RawIngredient2 objects for the SpecificIngredient
        objects, find the right ingredient by name.
        """

        # Add RawIngredient2 objects from fixtures.

        # Only add the needed RawIngredient2 objects. This makes the code
        # both faster and more isolated. If new, buggy RawIngredient2 objects
        # are added to the fixtures, they should not cause problems in a test
        # where they are not even being used.
        list_rawingredient2_of_specific_ingredient = [
            'Rice, white, long-grain, regular, raw, unenriched',
            'Pea protein powder',
            'Calcium citrate'
        ]

        # Simulate clicking on the menu item "Ingredients"
        click_navbar_item(
            'id_menu_item_rawingredients2',
            self.browser,
            Keys,
            time,
        )

        # Simulate the user creating a new RawIngredient2 instance using
        # the form.

        # Add all ingredients from the list.
        for k in range(len(ingredient_dict_list)):

            # Only add the RawIngredient2 objects necessary for the full day
            # of eating.
            if ingredient_dict_list[k]['name'] not in \
                    list_rawingredient2_of_specific_ingredient:
                continue

            new_ingredient_button = self.browser.find_element_by_id(
                'id_button_new_rawingredient2'
            )
            new_ingredient_button.click()

            time.sleep(0.5)

            for key, value in ingredient_dict_list[k].items():
                # The is_public key relates to a boolean field which is not to
                # be filled out with text but checked instead.
                if key != 'is_public':
                    if value is not None:
                        self.browser.find_element_by_name(key).clear()
                        self.browser.find_element_by_name(key).send_keys(
                            str(value)
                        )
                # Since the is_public key is set to False by default and False
                # is the desired setting, it is not necessary to do anything.
                else:
                    pass

            # Simulate clicking the save button
            save_button = self.browser.find_element_by_id(
                'id_button_save_new_rawingredient2'
            )
            save_button.click()

            time.sleep(1)

            # Check if the RawIngredient2 instance is found in the database.
            rawingredient2_saved_object = RawIngredient2.objects.filter(
                name=ingredient_dict_list[k]['name']
            )
            rawingredient2_was_saved = rawingredient2_saved_object.exists()
            self.assertTrue(rawingredient2_was_saved)

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

        nutrient_profile_name = 'Nutrient profile with missing values'

        self.browser.find_element_by_id('id_name').send_keys(
            nutrient_profile_name
        )

        # Set a value for calcium, leave everything else empty. Calories and
        # protein have to be empty, the rest does not matter.
        self.browser.find_element_by_id('id_calcium').send_keys(
            str(950)
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

        # Add nutrient targets.

        # Add calories.
        select_nutrient_target_0 = Select(self.browser.find_element_by_id(
            'id_specificnutrienttarget_set-0-nutrient_target'
        ))
        select_nutrient_target_0.select_by_visible_text(
            'calories'
        )
        # Simulate clicking the save button
        save_changes_button = self.browser.find_element_by_id(
            'save_changes_formset_fulldayofeating'
        )
        save_changes_button.click()
        time.sleep(0.5)

        # Add protein.
        select_nutrient_target_1 = Select(self.browser.find_element_by_id(
            'id_specificnutrienttarget_set-1-nutrient_target'
        ))
        select_nutrient_target_1.select_by_visible_text(
            'protein'
        )
        # Simulate clicking the save button
        save_changes_button = self.browser.find_element_by_id(
            'save_changes_formset_fulldayofeating'
        )
        save_changes_button.click()
        time.sleep(0.5)

        # Add calcium.
        select_nutrient_target_2 = Select(self.browser.find_element_by_id(
            'id_specificnutrienttarget_set-2-nutrient_target'
        ))
        select_nutrient_target_2.select_by_visible_text(
            'calcium'
        )
        # Simulate clicking the save button
        save_changes_button = self.browser.find_element_by_id(
            'save_changes_formset_fulldayofeating'
        )
        save_changes_button.click()
        time.sleep(0.5)

        # Add specific ingredients.
        for k in range(len(list_rawingredient2_of_specific_ingredient)):
            # Choose the RawIngredient2 object for each SpecificIngredient.
            id_rawingredient2_for_specificingredient = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-rawingredient'
            select_rawingredient2 = Select(self.browser.find_element_by_id(
                id_rawingredient2_for_specificingredient
            ))
            select_rawingredient2.select_by_visible_text(
                list_rawingredient2_of_specific_ingredient[k]
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
                'independent'
            )

            # Simulate clicking the save button
            save_changes_button = self.browser.find_element_by_id(
                'save_changes_formset_fulldayofeating'
            )
            save_changes_button.click()
            time.sleep(0.5)

        # Click the button 'Calculate full day of eating'.
        calculate_button = self.browser.find_element_by_id(
            'id_button_calculate_full_day_of_eating'
        )
        calculate_button.click()

        # Test whether the appropriate error page is shown.
        error_paragraph = self.browser.find_elements_by_id(
            'NoValueForTargetedNutrientError'
        )
        error_page_is_shown = \
            len(error_paragraph) > 0
        self.assertTrue(error_page_is_shown)

        # Get the text of the error message.
        error_message = self.browser.find_element_by_xpath(
            "//p[1]"
        )
        error_message_text = error_message.text
        self.assertIn('calories', error_message_text)
        self.assertIn('protein', error_message_text)
        self.assertNotIn('calcium', error_message_text)
