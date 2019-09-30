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
# from measuredfood.utils.set_to_zero_if_none import set_to_zero_if_none

# import the ingredient dictionaries
import sys

sys.path.insert(0, '/projectmf/data/')


class FullDayOfEatingPercentMaxTest(FunctionalTestWithUserLoggedIn):

    def test_calculate_full_day_of_eating_percent_max(self):
        """
        A full day of eating is calculated. Its total nutrition is
        calculated. For each nutrient sum, the ratio to the maximum amount of
        that nutrient is calculated and expressed as a percentage (% Max).

        It is tested whether the percentage of the maximum amount is
        calculated and displayed correctly.

        This might be equivalent to test_calculate_fulldayofeating_good_case.
        """

        list_nutrient_targets = []

        list_specificingredient = [
            {
                'rawingredient2': 'Walnuts',
                'amount': 45,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Mushrooms',
                'amount': 450,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Beer, alcohol free',
                'amount': 300,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Tomato puree, MUTTI',
                'amount': 350,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Pea protein powder',
                'amount': 200,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Rice, white, long-grain, regular, '
                                  'raw, unenriched',
                'amount': 200,
                'scaling_option': 'fixed',
            },
            {
                'rawingredient2': 'Kidney Beans, raw',
                'amount': 200,
                'scaling_option': 'fixed',
            },
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

        for specificingredient_dict_k in list_specificingredient:

            new_ingredient_button = self.browser.find_element_by_id(
                'id_button_new_rawingredient2'
            )
            new_ingredient_button.click()

            time.sleep(0.5)

            # Get the entry in ingredient_dict_list corresponding to
            # specificingredient_dict_k.

            rawingredient2_dict = next(
                item for item in ingredient_dict_list if
                item["name"] == specificingredient_dict_k['rawingredient2']
            )

            for key, value in rawingredient2_dict.items():
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
                name=rawingredient2_dict['name']
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

        new_nutrient_profile_button = self.browser.find_element_by_id(
            'id_button_new_nutrient_profile'
        )
        new_nutrient_profile_button.click()

        time.sleep(0.1)

        nutrient_profile_dict = \
            {
                'name': 'Maintenance EU',
                # source:
                #  https://www.efsa.europa.eu/en/interactive-pages/drvs
                'calories': 2500,  # 'default_unit': 'kcal'
                'carbohydrates': None,  # 'default_unit': 'gram'
                'fat': None,  # 'default_unit': 'gram'
                'protein': 164,  # 'default_unit': 'gram'
                # The values for linoleic acid and alpha linoleic acid were
                # given as
                # percentages of total energy intake. I went with values that
                # I had
                # noted in food_numbers_object_oriented that were taken from
                # wikipedia.
                'linoleic_acid': 17,  # 'default_unit': 'gram'
                'alpha_linoleic_acid': 1.6,  # 'default_unit': 'gram'
                # Vitamin A unit conversion:
                # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg
                # retinol,
                # or of 0.6 mcg beta-carotene
                # Source: https://dietarysupplementdatabase.usda.nih.gov/
                # ingredient_calculator/help.php
                # => * 0.3
                'vitamin_a': 750,  # 'default_unit': 'microgram'.
                'vitamin_c': 110,  # 'default_unit': 'milligram'
                'vitamin_d': 15,  # 'default_unit': 'microgram'
                'vitamin_e': 13,  # 'default_unit': 'milligram'
                'vitamin_k': 70,  # 'default_unit': 'microgram'
                # Thiamin intake is dependent on caloric intake. Went with a
                # value on
                # the high side for 3500 kcal.
                'thiamin': 1.5,  # 'default_unit': 'milligram'
                'riboflavin': 1.6,  # 'default_unit': 'milligram'
                # Niacin intake is dependent on caloric intake. Went with a
                # value on
                # the high side for 3500 kcal.
                'niacin': 24,  # 'default_unit': 'milligram'
                'vitamin_b6': 1.7,  # 'default_unit': 'milligram'
                'folate': 330,  # 'default_unit': 'microgram'
                'vitamin_b12': 4,  # 'default_unit': 'microgram'
                'pantothenic_acid': 5,  # 'default_unit': 'milligram'
                'biotin': 40,  # 'default_unit': 'microgram'
                'choline': 400,  # 'default_unit': 'milligram'
                'calcium': 950,  # 'default_unit': 'milligram'
                'chromium': None,  # 'default_unit': 'microgram'
                'copper': 1600,  # 'default_unit': 'microgram'
                'iodine': 150,  # 'default_unit': 'microgram'
                'iron': 11,  # 'default_unit': 'milligram'
                'magnesium': 350,  # 'default_unit': 'milligram'
                'manganese': 3,  # 'default_unit': 'milligram'
                'molybdenum': 65,  # 'default_unit': 'microgram'
                'phosphorus': 550,  # 'default_unit': 'milligram'
                'selenium': 70,  # 'default_unit': 'microgram'
                # Zinc PRI depends on phytate intake! Went with maximum.
                'zinc': 16.3,  # 'default_unit': 'milligram'
                'potassium': 3.500,  # 'default_unit': 'gram'
                'sodium': 2,  # 'default_unit': 'gram'
                'chloride': 3.1,  # 'default_unit': 'gram'

                # Maximum amounts (i.e. tolerable upper intake)
                'max_calories': None,  # 'default_unit': 'kcal'
                'max_carbohydrates': None,  # 'default_unit': 'gram'
                'max_fat': None,  # 'default_unit': 'gram'
                'max_protein': None,  # 'default_unit': 'gram'
                'max_linoleic_acid': None,  # 'default_unit': 'gram'
                'max_alpha_linoleic_acid': None,  # 'default_unit': 'gram'
                # Vitamin A unit conversion:
                # Vitamin A: 1 IU is the biological equivalent of 0.3
                # mcg retinol,
                # or of 0.6 mcg beta-carotene
                # Source: https://dietarysupplementdatabase.usda.nih.gov/
                # ingredient_calculator/help.php
                # => * 0.3
                'max_vitamin_a': 3000,  # 'default_unit': 'microgram'.
                'max_vitamin_c': None,  # ND  # 'default_unit': 'milligram'
                'max_vitamin_d': 100,  # 'default_unit': 'microgram'
                'max_vitamin_e': 300,  # 'default_unit': 'milligram'
                'max_vitamin_k': None,  # ND  # 'default_unit': 'microgram'
                'max_thiamin': None,  # ND  # 'default_unit': 'milligram'
                'max_riboflavin': None,  # ND  # 'default_unit': 'milligram'
                # The max for Niacin is for Nicotinamide. There is a different
                # TUI for
                # nicotinic acid.
                'max_niacin': 900,  # 'default_unit': 'milligram'
                'max_vitamin_b6': 25,  # 'default_unit': 'milligram'
                'max_folate': 1000,  # 'default_unit': 'microgram'
                'max_vitamin_b12': None,  # ND # 'default_unit': 'microgram'
                'max_pantothenic_acid': None,
                # ND  # 'default_unit': 'milligram'
                'max_biotin': None,  # ND  # 'default_unit': 'microgram'
                'max_choline': None,  # ND  # 'default_unit': 'milligram'
                'max_calcium': 2500,  # 'default_unit': 'milligram'
                'max_chromium': None,  # 'default_unit': 'microgram'
                'max_copper': 5000,  # 'default_unit': 'microgram'
                'max_iodine': 600,  # 'default_unit': 'microgram'
                'max_iron': None,  # ND  # 'default_unit': 'milligram'
                'max_magnesium': 250,  # specifically from
                # supplements, that is why it is higher than the amount in the
                # nutrient profile.  # 'default_unit': 'milligram'
                'max_manganese': None,  # ND  # 'default_unit': 'milligram'
                'max_molybdenum': 600,  # 'default_unit': 'microgram'
                'max_phosphorus': None,  # ND  # 'default_unit': 'milligram'
                'max_selenium': 300,  # 'default_unit': 'microgram'
                'max_zinc': 25,  # 'default_unit': 'milligram'
                'max_potassium': None,  # ND  # 'default_unit': 'gram'
                'max_sodium': None,  # 'default_unit': 'gram'
                'max_chloride': None,  # 'default_unit': 'gram'
            }

        for key, value in nutrient_profile_dict.items():
            if value is not None:
                self.browser.find_element_by_id(
                    'id_'+key
                ).clear()
                self.browser.find_element_by_id(
                    'id_'+key
                ).send_keys(str(value))

        # Simulate clicking the save button
        save_button = self.browser.find_element_by_id(
            'id_button_save_new_nutrientprofile'
        )
        save_button.click()

        time.sleep(1)

        # Test whether the saved nutrient profile is in the database.
        nutrient_profile_query = NutrientProfile.objects.filter(
            name=nutrient_profile_dict['name']
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

        name_dummy_full_day_of_eating = 'Chili mushrooms'

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
            nutrient_profile_dict['name']
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
        for k in range(len(list_specificingredient)):
            specificingredient_dict_k = list_specificingredient[k]
            # Choose the RawIngredient2 object for each SpecificIngredient.
            id_rawingredient2_for_specificingredient = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-rawingredient'
            select_rawingredient2 = Select(self.browser.find_element_by_id(
                id_rawingredient2_for_specificingredient
            ))
            select_rawingredient2.select_by_visible_text(
                specificingredient_dict_k['rawingredient2']
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
                specificingredient_dict_k['scaling_option']
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

        # Test whether the percentages of the maximum amount have been
        # calculated correctly.

        calories_and_default_units = [
            {'name': 'calories',
             'default_unit': 'kcal'},
        ]

        macronutrients_and_default_units = [
            # Matthias Schulz called it carbohydrates instead of carbohydrate
            # because that is what he is used to.
            {'name': 'carbohydrates',
             'default_unit': 'gram'},
            {'name': 'fat',
             'default_unit': 'gram'},
            {'name': 'protein',
             'default_unit': 'gram'},
        ]

        essential_fats_and_default_units = [
            {'name': 'linoleic_acid',
             'default_unit': 'gram'},
            {'name': 'alpha_linoleic_acid',
             'default_unit': 'gram'},
        ]

        vitamins_and_default_units = [
            {'name': 'vitamin_a',
             'default_unit': 'microgram'},
            {'name': 'vitamin_c',
             'default_unit': 'milligram'},
            {'name': 'vitamin_d',
             'default_unit': 'microgram'},
            {'name': 'vitamin_e',
             'default_unit': 'milligram'},
            {'name': 'vitamin_k',
             'default_unit': 'microgram'},
            {'name': 'thiamin',
             'default_unit': 'milligram'},
            {'name': 'riboflavin',
             'default_unit': 'milligram'},
            {'name': 'niacin',
             'default_unit': 'milligram'},
            {'name': 'vitamin_b6',
             'default_unit': 'milligram'},
            {'name': 'folate',
             'default_unit': 'microgram'},
            {'name': 'vitamin_b12',
             'default_unit': 'microgram'},
            {'name': 'pantothenic_acid',
             'default_unit': 'milligram'},
            {'name': 'biotin',
             'default_unit': 'microgram'},
            {'name': 'choline',
             'default_unit': 'milligram'},
        ]

        elements_and_default_units = [
            {'name': 'calcium',
             'default_unit': 'milligram'},
            {'name': 'chromium',
             'default_unit': 'microgram'},
            {'name': 'copper',
             'default_unit': 'microgram'},  # fluoride was removed
            {'name': 'iodine',
             'default_unit': 'microgram'},
            {'name': 'iron',
             'default_unit': 'milligram'},
            {'name': 'magnesium',
             'default_unit': 'milligram'},
            {'name': 'manganese',
             'default_unit': 'milligram'},
            {'name': 'molybdenum',
             'default_unit': 'microgram'},
            {'name': 'phosphorus',
             'default_unit': 'milligram'},
            {'name': 'selenium',
             'default_unit': 'microgram'},
            {'name': 'zinc',
             'default_unit': 'milligram'},
            {'name': 'potassium',
             'default_unit': 'gram'},
            {'name': 'sodium',
             'default_unit': 'gram'},
            {'name': 'chloride',
             'default_unit': 'gram'},
        ]

        all_nutrients_and_default_units = \
            calories_and_default_units \
            + macronutrients_and_default_units \
            + essential_fats_and_default_units \
            + vitamins_and_default_units \
            + elements_and_default_units

        for dict_k in all_nutrients_and_default_units:
            nutrient_name = dict_k['name']
            nutrition_content = self.browser.find_element_by_id(
                'nutrient content '+nutrient_name
            ).text

            nutrition_content = float(nutrition_content)

            if nutrient_profile_dict['max_'+nutrient_name] is None:
                continue

            percent_max_comparison_value = \
                nutrition_content \
                / nutrient_profile_dict['max_'+nutrient_name] \
                * 100

            percent_max_in_app_with_percent_symbol = \
                self.browser.find_element_by_id(
                    'percent max '+nutrient_name
                ).text
            # The last two symbols of the string are removed to remove both
            # the percent symbol and the space.
            percent_max_in_app_without_percent_symbol = \
                percent_max_in_app_with_percent_symbol[:-2]
            percent_max_in_app = float(
                percent_max_in_app_without_percent_symbol
            )

            deviation = abs(percent_max_in_app - percent_max_comparison_value)

            tolerable_deviation = 5

            deviation_is_within_range = deviation < tolerable_deviation

            self.assertTrue(deviation_is_within_range)
