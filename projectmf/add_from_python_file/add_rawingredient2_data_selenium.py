from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# THIS WORKS EVEN THOUGH IT IS UNDERLINED! PYCHARM GETS THE IMPORT ERRORS WRONG!
# Here is more info https://stackoverflow.com/
# questions/41816973/modulenotfounderror-what-does-it-mean-main-is-not-a-package
# Sandor Clegane managed to get Pycharm to recognize the import by marking
# the data directory as a source. (Settings / Project structure )
from ingredients_data2 import function_in_ingredients_data2
from ingredients_data2 import ingredient_dict_list
from projectmf.functional_tests.utils.click_navbar_item import click_navbar_item
# import the ingredient dictionaries
import sys
sys.path.insert(0, '/projectmf/data/')

function_in_ingredients_data2()

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

# TODO: Sandor Clegane wanted to import the click_navbar_item function from
#  projectmf/functional_tests/utils/click_navbar_item.py but could not figure
#  out how to import from there.


def click_navbar_item(
    id_,
    browser_,
    keys,
    time_,
):
    # Click on the navbar toggle element to show the menu items.
    navbar_toggle_button = browser_.find_element_by_class_name(
        'navbar-toggler'
        )
    navbar_toggle_button.send_keys(keys.ENTER)

    time_.sleep(1)

    button = browser_.find_element_by_id(id_)
    button.click()


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
                # Remove the default value from the field, if necessary.
                browser. \
                    find_element_by_name(key).clear()
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
