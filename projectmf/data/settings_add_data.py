"""
During development, the database will be dropped and recreated from time to
time. Therefore, Sandor's ingredients, full days of eating etc. are saved in
the data directory and added to the measuredfood web app using selenium.

This file contains the settings for adding the data to the measuredfood web
app using selenium.
"""

ALL_URLS_ADD_DATA = {
    'local': "http://127.0.0.1:8000/",
    'production': "https://measuredfood4875.eu.pythonanywhere.com/",
}

case = 'production'

URL_ADD_DATA = ALL_URLS_ADD_DATA[case]
USERNAME = 'sandor'
EMAIL = 'sandor.clegane.a@gmail.com'
PASSWORD_ALL = {
    'local': 'testpassword',
    'production': '//61?busy?CENTURY?exciting?07//',
}
PASSWORD = PASSWORD_ALL[case]
