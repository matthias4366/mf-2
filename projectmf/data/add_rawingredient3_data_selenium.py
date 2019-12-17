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

browser.find_element_by_id(
    'id_button_get_from_food_data_central'
).click()

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
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },
    {
        'id_ingredient_usda_api': None,
        'ingredient_name_usda_api': None,
    },

]

# Simulate the user creating a new RawIngredient3 using the FoodData Central
# database.
id_ = 'id_FDC_ID'
name_food_data_central_id_field = 'FDC_ID'
for ingredient in ingredients_to_get_from_food_data_central:

    if ingredient['id_ingredient_usda_api'] is None:
        continue

    # Enter the ingredient id.

    # Remove the default value from the field, if necessary. This should not
    # be necessary, as the initial value has been removed - but it remains as
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

time.sleep(10)
browser.quit()
