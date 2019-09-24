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


class JudgeTotalNutritionFullDayOfEatingTest(FunctionalTestWithUserLoggedIn):

    def test_judge_total_nutrition_full_day_of_eating(self):
        """
        A full day of eating is calculated. Its total nutrition is
        calculated. For each nutrient sum, the ratio to the maximum amount of
        that nutrient is calculated and expressed as a percentage (% Max).
        Additionally, the ratio of each nutrient sum to the target amount is
        calculated and expressed as a percentage (% Target).

        Based on '% Target' and '% Max', the total amount for that nutrient
        is judged to be either too little, good or too much.

        It is tested whether the correct judgement is displayed.

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

        # The test is set up in such a way as to force certain judgments. The
        # judgments are forced by producing specific combinations of '%
        # target' and '% max'.
        # To achieve the desired values for '% target' and '% max',
        # the nutrient profile is set up artifically to produce these values.
        # The total for every nutrient is needed for this calculation (e.g.
        # 2711.5 kcal). These are obtained from calculating the full day of
        # eating in the measured food app.

        right_amount_str = 'good'
        too_much_str = 'too much'
        too_little_str = 'too little'
        error_message = 'Error: % target <= % max.'

        desired_results_total_nutrition_full_day_of_eating = \
            [
                {
                    'nutrient_name': 'calories',
                    'sum': 2711.5,
                    'percent_target': None,
                    'percent_max': None,
                    'judgment': right_amount_str,
                },
                {
                    'nutrient_name': 'carbohydrates',
                    'sum': 355.3,
                    'percent_target': None,
                    'percent_max': 50,
                    'judgment': right_amount_str,
                },
                {
                    'nutrient_name': 'fat',
                    'sum': 45,
                    'percent_target': None,
                    'percent_max': 150,
                    'judgment': too_much_str,
                },
                {
                    'nutrient_name': 'protein',
                    'sum': 236.8,
                    'percent_target': 50,
                    'percent_max': None,
                    'judgment': too_little_str,
                },
                {
                    'nutrient_name': 'linoleic_acid',
                    'sum': 18.8,
                    'percent_target': 50,
                    'percent_max': 40,
                    'judgment': too_little_str,
                },
                {
                    'nutrient_name': 'alpha_linoleic_acid',
                    'sum': 4.9,
                    'percent_target': 50,
                    'percent_max': 150,
                    'judgment': error_message,
                },
                {
                    'nutrient_name': 'vitamin_a',
                    'sum': 544.5,
                    'percent_target': 150,
                    'percent_max': None,
                    'judgment': right_amount_str,
                },
                {
                    'nutrient_name': 'vitamin_c',
                    'sum': 56.1,
                    'percent_target': 150,
                    'percent_max': 50,
                    'judgment': right_amount_str,
                },
                {
                    'nutrient_name': 'vitamin_d',
                    'sum': 81.0,
                    'percent_target': 150,
                    'percent_max': 140,
                    'judgment': too_much_str,
                },
                {
                    'nutrient_name': 'vitamin_e',
                    'sum': 7.9,
                    'percent_target': 100,
                    'percent_max': 100,
                    'judgment': error_message,
                },
                # {
                #     'nutrient_name': ,
                #     'sum': ,
                #     'percent_target': ,
                #     'percent_max': ,
                #     'judgment': ,
                # },
            ]

        nutrient_profile_dict = {}

        for dict_k in desired_results_total_nutrition_full_day_of_eating:

            if dict_k['percent_target'] is None:
                target_amount = None
            else:
                target_amount = (dict_k['sum']/dict_k['percent_target']) * 100

            if dict_k['percent_max'] is None:
                max_amount = None
            else:
                max_amount = (dict_k['sum']/dict_k['percent_max']) * 100

            new_dict = {
                dict_k['nutrient_name']: target_amount,
                'max_'+dict_k['nutrient_name']: max_amount,
            }

            nutrient_profile_dict.update(new_dict)

        # Add name to nutrient profile:
        nutrient_profile_dict.update(
            {'name': 'Nutrientprofile artifically created to produce given '
                     'percent target and percent max values.'}
        )

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

        # The user is redirected to the list of full days of eating.
        # Find the correct full day of eating and click the edit button.
        edit_button = self.browser.find_element_by_id(
            'edit ' + name_dummy_full_day_of_eating
        )
        edit_button.click()

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

            # Enter the base amounts.
            id_base_amount_specificingredient = \
                'id_specificingredient_set-' \
                + str(k) \
                + '-base_amount'
            base_amount_field = self.browser.find_element_by_id(
                id_base_amount_specificingredient
            )
            base_amount_field.clear()
            base_amount_field.send_keys(specificingredient_dict_k['amount'])

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

        # Test whether the judgement is displayed correctly. This test does
        # not cover whether the calculation of the '% Target' and '% Max'
        # values is correct.

        for dict_k in desired_results_total_nutrition_full_day_of_eating:

            judgment_in_app = self.browser.find_element_by_id(
                'judgment '+dict_k['nutrient_name']
            ).text
            # print('Currently checking judgment for nutrient:')
            # print(dict_k['nutrient_name'])
            self.assertEqual(dict_k['judgment'], judgment_in_app)
            # print('Judgment was correct.')
