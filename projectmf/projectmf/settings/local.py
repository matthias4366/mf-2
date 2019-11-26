"""
Django settings for projectmf project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from .base import *

print('LOCAL SETTINGS ARE USED.')

# TODO: Use an environment variable for the secret key. This is for testing
#  purposes.
# SECRET_KEY = get_env_variable("SECRET_KEY_DEVELOPMENT")
SECRET_KEY = "nt@$w7%vl#&s^-66+^ill62$cmass8vpat)a(b2nt=9##=+__"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgresql_database_measured_food',
        'USER': 'user_matthias',
        'PASSWORD': get_env_variable("PASSWORD_DATABASE_DEVELOPMENT"),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
