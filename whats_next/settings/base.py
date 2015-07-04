# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .utils import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

##########################
# SECRET KEY CONFIGURATION

SECRET_KEY = get_env_setting('SECRET_KEY', error_msg='You need to set a secret key!')

# SECRET KEY CONFIGURATION
##########################


#####################
# DEBUG CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = str2bool(get_env_setting('DEBUG', default=False))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

# DEBUG CONFIGURATION
#####################

########################
# SECURITY CONFIGURATION

INTERNAL_IPS = ast.literal_eval(get_env_setting('INTERNAL_IPS', default="('127.0.0.1',)"))

# SECURITY CONFIGURATION
########################


#######################
# MANAGER CONFIGURATION

# See: # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Joseph Bennett', 'josephbennett42@gmail.com'),
)

# See: # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# MANAGER CONFIGURATION
#######################

###################
# APP CONFIGURATION

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# APP CONFIGURATION
###################

ROOT_URLCONF = 'whats_next.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'whats_next.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
