from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from click_navbar_item_copy import click_navbar_item
from selenium.common.exceptions import NoSuchElementException
from initial_nutrient_profiles import nutrient_profile_dict_list
# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')

"""
During development, from time to time the database will be deleted and 
recreated, and thus its contents will be lost. Sandor clegane is using 
the application for his daily needs and thus loses his saved RawIngredient2, 
FullDayOfEating and Mealplanobjects. The first attempted solution 
consisted of fixtures. However, these proved problematic, as RawIngredient2 
objects added from fixtures would not have the same IDs as the original 
RawIngredient2 objects. Thus, the SpecificIngredient objects in the 
FullDayOfEating objects would reference the WRONG RawIngredient2 object. 
To mitigate this problem, new code was written.

This part of the new code adds the mealplan.
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

click_navbar_item(
    'id_menu_item_nutrient_profiles',
    browser,
    Keys,
    time,
)

# Add the nutrient profiles.

for k in range(len(nutrient_profile_dict_list)):

    # See if the nutrient profile already exists. If so, delete it.
    try:
        nutrient_profile_name = \
            browser.find_element_by_id(
                'paragraph ' + nutrient_profile_dict_list[k]['name'])
        try:
            browser.find_element_by_id(
                'delete ' + nutrient_profile_dict_list[k]['name']).click()
            browser.find_element_by_id(
                'confirm_delete').click()
            time.sleep(0.5)
        except NoSuchElementException:
            print('Element not found. Not supposed to happen.')
            break
    except NoSuchElementException:
        pass

    browser.find_element_by_id(
        'id_button_new_nutrient_profile'
    ).click()

    time.sleep(0.1)

    for key, value in nutrient_profile_dict_list[k].items():
        id_from_key = 'id_' + key
        if value is not None:
            browser.find_element_by_id(id_from_key).send_keys(
                str(value)
            )

    # Simulate clicking the save button
    save_button = browser.find_element_by_id(
        'id_button_save_new_nutrientprofile'
    )
    save_button.click()

    time.sleep(0.5)


# Tear it down
time.sleep(10)
browser.quit()
