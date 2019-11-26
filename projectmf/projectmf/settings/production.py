from .base import *

print('PRODUCTION SETTINGS ARE USED.')

# TODO: Get the secret key from an environment variable!
# SECRET_KEY = get_env_variable("SECRET_KEY_PRODUCTION")
SECRET_KEY = "nt@$w7%vl#&s^-66+^ill62$cmass8vpat)a(b2nt=9##=+__"

DEBUG = False

ALLOWED_HOSTS = [
    'tailoredmealplans.pythonanywhere.com'
]

# Security settings:
# Set for 12 hours, so, if I fuck things up, I can continue tomorrow.
SECURE_HSTS_SECONDS = 43200
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

# As far as Sandor Clegane understands it from
# https://docs.djangoproject.com/en/2.2/topics/security/#ssl-https,
# this line ensures that requests over HTTP are redirected to HTTPS.
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

# Sandor Clegane chose the careful, historical option.
# To improve performance, set to None or a positive number.
CONN_MAX_AGE = 0

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'measuredfooddb',
        'USER': 'measuredfooduser',
        'PASSWORD': get_env_variable("DATABASE_PASSWORD_PRODUCTION"),
        'HOST': 'measuredfood4875-23.postgres.eu.pythonanywhere-services.com',
        'PORT': '10023',
    }
}
