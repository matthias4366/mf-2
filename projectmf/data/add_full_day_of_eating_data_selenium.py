from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# IT WORKS DESPITE BEING MARKED AS WRONG!
# It is not marked as wrong if the data directory is added to the sources in
# Pycharm -> Settings -> Project Structure.
from click_navbar_item_copy import \
    click_navbar_item
from selenium.common.exceptions import NoSuchElementException
# IT WORKS DESPITE BEING MARKED AS WRONG!
from initial_full_day_of_eating_data import \
    full_day_of_eating_dict_list

"""
During development, from time to time the database will be deleted and 
recreated, and thus its contents will be lost. Sandor clegane is using 
the application for his daily needs and thus loses his saved RawIngredient2 
objects and his saved FullDayOfEating objects. The first attempted solution 
consisted of fixtures. However, these proved problematic, as RawIngredient2 
objects added from fixtures would not have the same IDs as the original 
RawIngredient2 objects. Thus, the SpecificIngredient objects in the 
FullDayOfEating objects would reference the WRONG RawIngredient2 object. To 
mitigate this problem, this script is written to add the RawIngredient2 
objects in a way that will always work properly.
"""

browser = webdriver.Firefox()

browser.get(URL_ADD_DATA)

# Log In

# Click navbar toggle

navbar_toggle = browser.find_element_by_class_name('navbar-toggler')
navbar_toggle.click()

login_menu_option = browser.find_element_by_link_text('Login')
login_menu_option.click()

# Find login elements
username_field = browser.find_element_by_name('username')
password_field = browser.find_element_by_name('password')

# Input values into the fields
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Simulate clicking on Log In
click_navbar_item(
    'id_button_login',
    browser,
    Keys,
    time,
)

# Add the full days of eating.

# Simulate clicking on the menu item "Ingredients"
click_navbar_item(
    'id_menu_item_fulldayofeating',
    browser,
    Keys,
    time,
)

for k in range(0, len(full_day_of_eating_dict_list)):

    # Check if the full day of eating exists already. If so, delete it.
    try:
        full_day_of_eating_name = \
            browser.find_element_by_id(
                'paragraph ' + full_day_of_eating_dict_list[k]['name'])
        try:
            browser.find_element_by_id(
                'delete ' + full_day_of_eating_dict_list[k]['name']).click()
            browser.find_element_by_id(
                'confirm delete ' + full_day_of_eating_dict_list[k][
                    'name']).click()
        except NoSuchElementException:
            print('Element not found. Not supposed to happen.')
            raise NoSuchElementException('Element not found. Not supposed to '
                                         'happen.')
    except NoSuchElementException:
        pass

    # This code assumes that all the ingredients necessary for the
    # FullDayOfEating object are already present.

    # Create new FullDayOfEating.
    button_new_full_day_of_eating = browser.find_element_by_id(
        'id_button_new_fulldayofeating'
    )
    button_new_full_day_of_eating.click()

    # Fill in the data.
    name_field = browser.find_element_by_id(
        'id_name'
    )
    name_field.send_keys(full_day_of_eating_dict_list[k]['name'])
    cooking_instruction_field = browser.find_element_by_id(
        'id_cooking_instruction'
    )
    cooking_instruction_field.send_keys(
        full_day_of_eating_dict_list[k]['cooking_instruction']
    )

    # Select the nutrient profile

    select_nutrient_profile = Select(browser.find_element_by_id(
        'id_nutrient_profile'
    ))
    select_nutrient_profile.select_by_visible_text(
        full_day_of_eating_dict_list[k]['nutrient_profile']
    )

    save_full_day_of_eating_button = browser.find_element_by_id(
        'id_button_save_new_fulldayofeating'
    )
    save_full_day_of_eating_button.click()

    time.sleep(0.5)

    # Set the nutrient targets for the calculation.

    for l in range(len(full_day_of_eating_dict_list[k][
                           'list_nutrient_target'])):
        select_nutrient_target = Select(browser.find_element_by_id(
            'id_specificnutrienttarget_set-'
            + str(l)
            + '-nutrient_target'
        ))
        select_nutrient_target.select_by_visible_text(
            full_day_of_eating_dict_list[k][
                'list_nutrient_target'][l]
        )

        browser.find_element_by_id(
            'save_changes_formset_fulldayofeating'
        ).click()

    # Add the SpecificIngredient objects.

    for m in range(len(full_day_of_eating_dict_list[k]
                       ['list_dict_specific_ingredient'])):
        # Amount.
        browser.find_element_by_id(
            'id_specificingredient_set-'
            + str(m)
            + '-base_amount'
        ).clear()
        browser.find_element_by_id(
            'id_specificingredient_set-'
            + str(m)
            + '-base_amount'
        ).send_keys(
            str(
                full_day_of_eating_dict_list[k]
                ['list_dict_specific_ingredient'][m]['base_amount']
            )
        )

        # Unit.
        select_unit = Select(browser.find_element_by_id(
            'id_specificingredient_set-'
            + str(m)
            + '-base_amount_unit'
        ))
        select_unit.select_by_visible_text(
            full_day_of_eating_dict_list[k][
                'list_dict_specific_ingredient'][m]['base_amount_unit']
        )

        # Raw ingredient.
        select_rawingredient = Select(browser.find_element_by_id(
            'id_specificingredient_set-'
            + str(m)
            + '-rawingredient'
        ))
        select_rawingredient.select_by_visible_text(
            full_day_of_eating_dict_list[k][
                'list_dict_specific_ingredient'][m]['rawingredient']
        )

        # Scaling option.
        select_scaling_option = Select(browser.find_element_by_id(
            'id_specificingredient_set-'
            + str(m)
            + '-scaling_option'
        ))
        select_scaling_option.select_by_visible_text(
            full_day_of_eating_dict_list[k][
                'list_dict_specific_ingredient'][m]['scaling_option']
        )

        browser.find_element_by_id(
            'save_changes_formset_fulldayofeating'
        ).click()

    browser.find_element_by_id(
        'id_button_back_to_list_of_full_days_of_eating'
    ).click()

# Tear it down
browser.quit()

