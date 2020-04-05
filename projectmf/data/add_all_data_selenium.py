from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD

from add_fulldayofeating_data_selenium import add_fulldayofeating_data_selenium

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

# imports for add_nutrientprofile_selenium
from add_nutrientprofile_selenium import add_nutrientprofile_selenium
import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from settings_add_data import \
    URL_ADD_DATA, \
    USERNAME, \
    PASSWORD
from selenium import webdriver
import time
import json
from selenium.webdriver.common.keys import Keys
from click_navbar_item_copy import click_navbar_item
from selenium.common.exceptions import NoSuchElementException
sys.path.insert(0, '/projectmf/data/')

"""
During development, from time to time the database will be deleted and 
recreated, and thus its contents will be lost. 

Hence, the data necessary to build the Mealplan of Sandor is stored locally 
in the form of Python dictionaries and JSON files.

This script adds the data from the locally stored Python dictionaries into 
the measured food web app, either into the local one or into the one hosted 
on pythonanywhere.

Previously, each model had its own script for this purpose:
add_full_day_of_eating_data_selenium.py
add_mealplan_data_selenium.py
add_nutrientprofile_selenium.py
add_rawingredient3_data_selenium.py

This script will merge all the functionality into one place so everything can
be run with one click.
"""

add_nutrientprofile_selenium(
    webdriver,
    URL_ADD_DATA,
    USERNAME,
    PASSWORD,
    click_navbar_item,
    Keys,
    time,
    json,
    NoSuchElementException,
)


# add_fulldayofeating_data_selenium(
#     webdriver,
#     URL_ADD_DATA,
#     USERNAME,
#     PASSWORD,
#     click_navbar_item,
#     Keys,
#     time,
#     full_day_of_eating_dict_list,
#     NoSuchElementException,
#     Select,
# )
