"""
Django settings for jas project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,sys
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARTIT_DIR = os.path.split(os.path.dirname(__file__))[0]
sys.path = [CHARTIT_DIR] + sys.path

PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+s=7xbr5qeqw7ob^uzhn^@&zyc%#iq7*%k+%&!04%$jsz%d%s%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CHARTIT_JS_REL_PATH = '/chartit/js/'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'datadb',
    'prognoz',
    'maps',
    'gismap',
    'django_tables2',
    'django.contrib.gis',
    'djgeojson',
    'leaflet',
    'chartit',
    'sorl.thumbnail',
    'rest_framework',
    'datetimewidget',
     )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
   )

ROOT_URLCONF = 'jas.urls'


TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]




WSGI_APPLICATION = 'jas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
     'other': {
        'NAME': '_GMC',
        'ENGINE': 'sql_server.pyodbc',
        'USER': "gmcreader",
        'PASSWORD': "123",
        'HOST': "MSSQL-PYTHON",                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': "1433",                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
                'host_is_server': False,
                'dsn': "MSSQL-PYTHON",
        },

     },
      'newgis':{
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR,'..', 'data.db'),
      },


 }

DATABASE_NAME = 'GIDRO'
DATABASE_HOST = 'MSSQL-PYTHON'
DATABASE_PORT = '1433'
DATABASE_USER = 'gmcreader'
DATABASE_PASSWORD = '123'
DATABASE_OPTIONS = {
        'host_is_server': False,
        'dsn': 'MSSQL-PYTHON',
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


TEMPLATES_DIR=(
    join(PROJECT_ROOT,'templates'),
)

MEDIA_ROOT = PROJECT_ROOT

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = '/home/alex/Auto/jas/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR,'static_root'))


LEAFLET_CONFIG = {

 'SPATIAL_EXTENT': (24.0, 51.50, 28, 53.50),
 'DEFAULT_CENTER': (26.0, 52.00),
 'DEFAULT_ZOOM': 8,
 'MIN_ZOOM': 6,
 'MAX_ZOOM': 25,
 'ATTRIBUTION_PREFIX': 'Powered by django-leaflet',
 'TILES': [ ('Sputnik.ru','http://{s}.tiles.maps.sputnik.ru/tiles/kmt2/{z}/{x}/{y}.png',{}),
            ('OSM', 'http://tile.osm.org/{z}/{x}/{y}.png',{}),
            ('MapBox', 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {} ),
            ('Mapquest','https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}.png32?access_token=pk.eyJ1IjoicGF4YW5hbGV4IiwiYSI6ImNpczIyeDVtNDAwN3Myc283enQ4Zm90cnYifQ.nuqCc0opJDWu7QhG7fOaBw',{}),
            ( 'Esri Areal', 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {}) ,
	         ]

}

