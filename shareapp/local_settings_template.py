import sys

__author__ = 'schien'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shareapp',
        'USER': 'shareapp',
        'HOST': 'localhost',
        'PORT': '',
        'PASSWORD': '',
    }
}

# disable south for testing
SOUTH_TESTS_MIGRATE = False # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True # To disable South's own unit tests
# - See more at: http://www.celerity.com/blog/2013/04/29/how-write-speedy-unit-tests-django-part-1-basics/#sthash.9vDnOgRl.dpuf
if 'test' in sys.argv: DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

ALLOWED_HOSTS = ['fritz', 'localhost', 'dgd', '127.0.0.1']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# for development without authentication
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#     # for web auth
#     # for oauth
#     #'rest_framework.authentication.OAuth2Authentication',
#     # 'rest_framework.authentication.BasicAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#     #'rest_framework.permissions.IsAuthenticated',
#     )
#
#     # 'PAGINATE_BY': 10
#
# }



try:
    from development_settings import *
except ImportError, e:
    print 'Unable to load local_settings.py:', e
