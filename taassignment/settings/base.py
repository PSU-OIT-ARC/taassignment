"""
Django settings for taassignment project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from fnmatch import fnmatch
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

DJANGO_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.normpath(os.path.join(DJANGO_DIR, "../"))

AUTH_USER_MODEL = 'users.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

ALLOWED_HOSTS = ['.pdx.edu']

# Application definition
# allow the use of wildcards in the INTERAL_IPS setting
class IPList(list):
    # do a unix-like glob match
    # E.g. '192.168.1.100' would match '192.*'
    def __contains__(self, ip):
        for ip_pattern in self:
            if fnmatch(ip, ip_pattern):
                return True
        return False

INTERNAL_IPS = IPList(['10.*', '192.168.*'])


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taassignment.users',
    'taassignment.course',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'taassignment.urls'

WSGI_APPLICATION = 'taassignment.wsgi.application'

# CAS authentication setting using djangocas
USE_CAS = True

if USE_CAS:
    CAS_SERVER_URL = 'https://sso.pdx.edu/cas/'

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'taassignment.backends.PSUBackend',
    )

    MIDDLEWARE_CLASSES += (
        'djangocas.middleware.CASMiddleware',
    )

## end CAS authentication setting

# LDAP support
LDAP_URL = "ldap://ldap-batch.oit.pdx.edu"
LDAP_BASE_DN = 'oc=people,dc=pdx,dc=edu'

ROOT_URLCONF = 'taassignment.urls'

WSGI_APPLICATION = 'taassignment.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/users/whg/'

# Absolute filesystem path to the directory that will hold user-uploaded files
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_DIR, "templates"),
)
