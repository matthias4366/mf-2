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


class FixedIngredientExceedsNutrientProfileValueTest(
        FunctionalTestWithUserLoggedIn):

    def test_fixed_ingredient_exceeds_nutrient_profile_value_error(self):
        """
        This test tests whether the
        FixedIngredientExceedsNutrientProfileValueError is
        displayed properly at the proper time.

        If the fixed ingredients already provide nutrition in excess of the
        values in the nutrient profile, it is impossible to find a positive
        result for the scaling ingredients that will bring the values down to
        the target levels.

        A full day of eating is set up in a way to force this error message
        to appear.

        It is tested whether the correct error message is displayed.
        """

        list_nutrient_targets = [
            'calories',
        ]

        list_nutrient_target_values = [
            10,
        ]

        list_rawingredient2_of_specific_ingredient = [
            'Pea protein powder',
            'Kidney Beans, raw',
        ]

        list_scaling_option = [
            'fixed',
            'independent',
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

        # The nutrient profile values are setup in a way to provoke a
        # negative result for the calculated amount of Pea protein powder.

        nutrient_profile_name = 'Low calorie target exceeded by fixed ' \
                                'ingredient'

        self.browser.find_element_by_id('id_name').clear()
        self.browser.find_element_by_id('id_name').send_keys(
            nutrient_profile_name
        )

        for k in range(len(list_nutrient_targets)):
            id_k = 'id_' + list_nutrient_targets[k]
            self.browser.find_element_by_id(id_k).clear()
            self.browser.find_element_by_id(id_k).send_keys(
                str(list_nutrient_target_values[k])
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

        # Click the button 'Calculate full day of eating'.
        calculate_button = self.browser.find_element_by_id(
            'id_button_calculate_full_day_of_eating'
        )
        calculate_button.click()

        # Test whether the appropriate error page is shown.
        error_paragraph = self.browser.find_elements_by_id(
            'FixedIngredientExceedsNutrientProfileValueError'
        )
        error_page_is_shown = \
            len(error_paragraph) > 0
        self.assertTrue(error_page_is_shown)
