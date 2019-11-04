from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from functional_tests.utils.click_navbar_item import \
    click_navbar_item
from selenium.common.exceptions import NoSuchElementException
from data.ingredients_data2 import ingredient_dict_list
# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')

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

# Wait until the FullDayOfEating objects have been saved in dictionaries.
# It is possible that recreating the ingredients will mess up the keys of the
# ingredients and thus mess up the full days of eating.

initial_full_day_of_eating_data_has_been_written = False

if initial_full_day_of_eating_data_has_been_written:

    # Add the ingredients.

    # Simulate clicking on the menu item "Ingredients"
    click_navbar_item(
        'id_menu_item_rawingredients2',
        browser,
        Keys,
        time,
    )

    # Simulate the user creating a new RawIngredient2 instance using
    # the form.

    # Add the all ingredients from the list.
    for k in range(0, len(ingredient_dict_list)):

        # Check if the ingredient exists already. If it does, delete it.
        # Existing RawIngredient2 objects that are not in the
        # ingredient_dict_list are not affected. The script does not delete all
        # previous RawIngredient2 objects.
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
            'id_button_new_rawingredient2'
        )
        new_ingredient_button.click()

        time.sleep(0.5)

        for key, value in ingredient_dict_list[k].items():
            # The is_public key relates to a boolean field which is not to
            # be filled out with text but checked instead.
            if key != 'is_public':
                if value is not None:
                    browser. \
                        find_element_by_name(key).send_keys(str(value))
            # Since the is_public key is set to False by default and False
            # is the desired setting, it is not necessary to do anything.
            else:
                pass

        # Simulate clicking the save button
        save_button = browser.find_element_by_id(
            'id_button_save_new_rawingredient2'
        )
        save_button.click()

# Tear it down
time.sleep(10)
browser.quit()

