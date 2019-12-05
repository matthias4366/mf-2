from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from click_navbar_item_copy import \
    click_navbar_item
from initial_mealplan_data import mealplan_initial_data

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
    'id_menu_item_mealplan',
    browser,
    Keys,
    time,
)

# Add all the mealplans (currently just one) from the stored data.

for k in range(len(mealplan_initial_data)):

    # If a mealplan with the same name exists, delete it.
    id_ = 'delete ' + mealplan_initial_data[k]['name']
    print('\n id_ \n')
    print(id_)
    try:
        browser.find_element_by_id(
            'delete ' + mealplan_initial_data[k]['name']).click()
        browser.find_element_by_id(
            'confirm delete ' + mealplan_initial_data[k][
                'name']).click()
    except NoSuchElementException:
        print('\n\n No mealplan with the same name found. \n\n')

    browser.find_element_by_id(
        'id_button_new_mealplan'
    ).click()

    browser.find_element_by_id(
        'id_name'
    ).send_keys(
        mealplan_initial_data[k]['name']
    )

    select_nutrient_profile = Select(browser.find_element_by_id(
        'id_nutrient_profile'
    ))
    select_nutrient_profile.select_by_visible_text(
        mealplan_initial_data[k]['nutrient_profile']
    )

    browser.find_element_by_id(
        'id_button_save_new_mealplan'
    ).click()

    for l in range(len(mealplan_initial_data[k]['fulldayofeating_list'])):
        select_fulldayofeating = Select(browser.find_element_by_id(
            'id_specificfulldayofeating_set-'
            + str(l)
            + '-fulldayofeating'
        ))
        select_fulldayofeating.select_by_visible_text(
            mealplan_initial_data[k]['fulldayofeating_list'][l]
        )

        browser.find_element_by_id(
            'save_changes_mealplan'
        ).click()

# Tear it down
browser.quit()
