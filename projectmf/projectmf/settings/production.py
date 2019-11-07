from .base import *

DEBUG = False

# Security settings:
# Set for 12 hours, so, if I fuck things up, I can continue tomorrow.
SECURE_HSTS_SECONDS = 43200
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'measuredfooddb',
        'USER': 'measuredfooduser',
        'PASSWORD': '//85=bread=BICYCLE=number=66//',
        'HOST': 'measuredfood4875-23.postgres.eu.pythonanywhere-services.com',
        'PORT': '10023',
    }
}
