from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from selenium.common.exceptions import NoSuchElementException
from data.initial_mealplan_data import mealplan_initial_data
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

browser.get("http://127.0.0.1:8000/")

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
username_field.send_keys('sandor')
password_field.send_keys('testpassword')

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

    try:
        mealplan_name = \
            browser.find_element_by_id(
                'paragraph ' + mealplan_initial_data[k]['name'])
        try:
            browser.find_element_by_id(
                'delete ' + mealplan_initial_data[k]['name']).click()
        except NoSuchElementException:
            print('Element not found. Not supposed to happen.')
            break
    except NoSuchElementException:
        pass

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
time.sleep(10)
browser.quit()
