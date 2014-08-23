# Django settings for greendoors project.
import os

PROJECT_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
# FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, '/api/test_fixtures'),)
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dan Schien', 'dschien@gmail.com'), )

MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587


# SSL settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['greendoors.cs.bris.ac.uk']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files sh be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = '/var/www/static/'
STATIC_ROOT = (os.path.join(PROJECT_ROOT, './../../WWW/static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/'),
    # os.path.join(PROJECT_ROOT, 'frome2014/app'),

    # os.path.join('/Users/schien/workspaces/cordova/bristol2014/appsrc'),
    # os.path.join(PROJECT_ROOT, 'web/build'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=@5)o*x-0q07%t7-50e)ni#*kobd=ekqb7&45_#@jdoy5(v@nb'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    # 'dbtemplates.loader.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # # TODO remove in prod
    # 'api.middleware.crossdomainxhr.XsSharing',
    # 'corsheaders.middleware.CorsMiddleware',
    # 'api.middleware.exceptionlog.ExceptionLoggingMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware'
)


#
# CORS_ORIGIN_WHITELIST = (
# 'http://localhost:8000'
# 'http://localhost:8002'
# )

# CORS_ALLOW_HEADERS = (
#    'accept',
#    'authorization',
#    'origin'
# )

# APPEND_SLASH = False

# # TODO remove
# XS_SHARING_ALLOWED_ORIGINS = "http://127.0.0.1:8888"
# XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

ROOT_URLCONF = 'shareapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'shareapp.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',

    'django_extensions',
    'rest_framework',

    # for oauth2
    # 'provider',
    # 'provider.oauth2',

    # apps

    'api',

    # for CORS
    # 'corsheaders',

    # for testing
    # 'sslserver',

    'registration',


    'social.apps.django_app.default',

    # test app
    # 'thirdauth'
)

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     # for web auth
    #     # for oauth
    #     # 'rest_framework.authentication.OAuth2Authentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
    ,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
    # 'PAGINATE_BY': 10

}


# SOCIAL AUTH CONFIG SECTION
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
# These URLs are used on different steps of the auth process, some for successful results and others for error situations.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email profile']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
# Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
# URL where the user will be redirected in case of an error
SOCIAL_AUTH_LOGIN_URL = '/accounts/login/'
# Is used as a fallback for LOGIN_ERROR_URL
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
# Used to redirect new registered users, will be used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined.
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'
# Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in). Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
# The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_INACTIVE_USER_URL = '/'
# Inactive users can be redirected to this URL when trying to authenticate.
# Successful URLs will default to SOCIAL_AUTH_LOGIN_URL while error URLs will fallback to SOCIAL_AUTH_LOGIN_ERROR_URL.

# Explicitly set user model if not standard
# SOCIAL_AUTH_USER_MODEL = 'foo.bar.User'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
logs_folder = os.path.join(PROJECT_ROOT, './logs/')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logs_folder + 'default.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['null'],  # Quiet by default!
            'propagate': False,
            'level': 'DEBUG',
        },
        'management_commands': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError, e:
    print 'Unable to load local_settings.py:', e