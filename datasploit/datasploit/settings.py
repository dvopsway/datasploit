"""
Django settings for datasploit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qkcs#c=&q0+=w-i+%mq)9h0hc7v=ntsiaxj)5vu2t6551@-q6i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'facebook',
    'homepage'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'datasploit.urls'

WSGI_APPLICATION = 'datasploit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
   'default' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'datasploit'
   }
}


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR , 'templates/' ),
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        "django.core.context_processors.request",
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR ,'static','static_root')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR ,'static','static_dirs'),
    ]

MEDIA_ROOT = '/media/'

MEDIA_URL = os.path.join(BASE_DIR ,'static','media/')

# MongoDB Server Details
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DATABASE = "datasploit"
