from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from ingredients_data3 import ingredient_dict_list

"""
During development, from time to time the database will be deleted and 
recreated, and thus its contents will be lost. Sandor clegane is using 
the application for his daily needs and thus loses his saved RawIngredient3 
objects and his saved FullDayOfEating objects. 

The RawIngredient3 objects will be added using the FoodData Central database.
This way, Sandor Clegane's use of the application closely mimics other user's 
use of the application.
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

# Add the ingredients.

# Simulate clicking on the menu item "Ingredients"
click_navbar_item(
    'id_menu_item_rawingredients3',
    browser,
    Keys,
    time,
)

template_ingredient = [
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
]

ingredients_to_get_from_food_data_central = [
    {
        'id_ingredient_usda_api': 169738,
        'ingredient_name_usda_api': 'Pasta, whole-wheat, dry (Includes foods '
                                    'for USDA\'s Food Distribution Program)',
    },
    {
        'id_ingredient_usda_api': 173744,
        'ingredient_name_usda_api': 'Beans, kidney, red, mature seeds, raw',
    },
    {
        'id_ingredient_usda_api': 169760,
        'ingredient_name_usda_api':
            'Rice, white, medium-grain, raw, unenriched',
    },
    {
        'id_ingredient_usda_api': 171328,
        'ingredient_name_usda_api': 'Spices, oregano, dried',
    },
    {
        'id_ingredient_usda_api': 168434,
        'ingredient_name_usda_api':
            'Mushrooms, brown, italian, or crimini, raw',
    },
    {
        'id_ingredient_usda_api': 170187,
        'ingredient_name_usda_api': 'Nuts, walnuts, english',
    },
    {
        'id_ingredient_usda_api': 554844,
        'ingredient_name_usda_api': 'NOW SPORTS, PEA PROTEIN',
    },
    {
        'id_ingredient_usda_api': 168462,
        'ingredient_name_usda_api': 'Spinach, raw',
    },
    {
        'id_ingredient_usda_api': 169998,
        'ingredient_name_usda_api': 'Corn, sweet, yellow, raw',
    },
    {
        'id_ingredient_usda_api': 175199,
        'ingredient_name_usda_api': 'Beans, pinto, mature seeds, '
                                    'raw (Includes foods for USDA\'s '
                                    'Food Distribution Program)',
    },
    {
        'id_ingredient_usda_api': 321900,
        'ingredient_name_usda_api': 'Broccoli, raw',
    },
    {
        'id_ingredient_usda_api': 170393,
        'ingredient_name_usda_api': 'Carrots, raw',
    },
    {
        'id_ingredient_usda_api': 170419,
        'ingredient_name_usda_api': 'Peas, green, raw',
    },
]

# Since Sandor is working on something else at the moment, this is 
# temporarily deactivated.
ingredients_are_added_from_food_data_central = False
if ingredients_are_added_from_food_data_central:
    browser.find_element_by_id(
        'id_button_get_from_food_data_central'
    ).click()

    # Simulate the user creating a new RawIngredient3 using the FoodData Central
    # database.
    id_ = 'id_FDC_ID'
    name_food_data_central_id_field = 'FDC_ID'
    for ingredient in ingredients_to_get_from_food_data_central:
    
        if ingredient['id_ingredient_usda_api'] is None:
            continue
    
        # Enter the ingredient id.
    
        # Remove the default value from the field, if necessary. This should not
        # be necessary, as the initial value has been removed - but it remains
        # as
        # a precaution.
        browser.find_element_by_id(
            'id_FDC_ID'
        ).clear()
    
        browser.find_element_by_id(
            'id_FDC_ID'
        ).send_keys(
            ingredient['id_ingredient_usda_api']
        )
    
        get_button = browser.find_element_by_id(
            'id_button_get_from_food_data_central'
        )
        get_button.click()

# Simulate clicking on the menu item "Ingredients"
click_navbar_item(
    'id_menu_item_rawingredients3',
    browser,
    Keys,
    time,
)

# Add the all ingredients from the list.
for k in range(0, len(ingredient_dict_list)):

    # Check if the ingredient exists already. If it does, delete it.
    # Existing RawIngredient3 objects that are not in the
    # ingredient_dict_list are not affected. The script does not delete all
    # previous RawIngredient3 objects.
    try:
        delete_button = \
            browser.find_element_by_id(
                'delete ' + ingredient_dict_list[k]['name']
            )
        delete_button.click()
        confirm_delete_button = browser.find_element_by_id(
            'confirm_delete'
        )
        confirm_delete_button.click()
        time.sleep(0.5)
    except NoSuchElementException:
        pass

    new_ingredient_button = browser.find_element_by_id(
        'id_button_new_rawingredient3'
    )
    new_ingredient_button.click()

    time.sleep(0.5)

    for key, value in ingredient_dict_list[k].items():
        if value is not None:
            # Remove the default value from the field, if necessary.
            browser. \
                find_element_by_name(key).clear()
            browser. \
                find_element_by_name(key).send_keys(str(value))

    # Simulate clicking the save button
    save_button = browser.find_element_by_id(
        'id_button_save_new_rawingredient3'
    )
    save_button.click()

time.sleep(10)
browser.quit()
