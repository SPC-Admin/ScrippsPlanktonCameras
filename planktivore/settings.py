"""
Django settings for planktivore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2$obh0g&szunx8*-mgv25-7_m-f%wjy=x13^qhglxzf81vt0ap'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ("127.0.0.1",)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'jquery',
    'rois',
    'roistats',
    'systemstats',
    'corsheaders',
    'django_mptt_admin',
    #'debug_toolbar',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'planktivore.urls'

WSGI_APPLICATION = 'planktivore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'planktivore_scripps_pier',
	'USER': 'ptvradmin',
	'PASSWORD': '$hmop3pod',
	'HOST': 'localhost',
	'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_URL = '/static/'

STATIC_URL = '/static/'
IMAGE_STORE = STATIC_URL + 'roistore/'
STATIC_ROOT = '/home/spcadmin/virtualenvs/planktivore/planktivore_scripps_pier/static/'
IMAGE_STORE_FULL_PATH = STATIC_ROOT + 'roistore/'
TMP_ARCHIVE_ROOT = STATIC_ROOT + 'roistore/TMP'
TMP_ARCHIVE_URL = STATIC_URL + 'roistore/TMP'
BACKUP_IMAGE_PATH = '/home/spcadmin/virtualenvs/planktivore/planktovore_scripps_pier/static/roistore/backups/'

TMP_ARCHIVE_ROOT = STATIC_ROOT + 'roistore/TMP'
TMP_ARCHIVE_URL = STATIC_URL + 'roistore/TMP'

SAVE_MORPH = False
MORPH_DIR = STATIC_ROOT + 'morph'
ID_DIR = MORPH_DIR
#BACKUP_IMAGE_PATH = '/data/home/spcadmin/backups/'

#STATICFILES_DIRS = (
#        os.path.join(BASE_DIR,'static'),
#)

REST_FRAMEWORK = {
#        'DEFAULT_PERMISSION_CLASSES': [
#            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#        ],
#        'DEFAULT_AUTHENTICATION_CLASSES': (
#            'rest_framework.authentication.SessionAuthentication',
#        ),
        #'PAGINATE_BY': 5000,
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 500
}

CORS_ORIGIN_ALLOW_ALL = True

MAP_USER_NAME = 'spcbridge'
MAP_USER_PASSWORD = 'c4lanu$'
