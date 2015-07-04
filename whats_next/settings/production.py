from .base import *


#####################
# DEBUG CONFIGURATION

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# DEBUG CONFIGURATION
#####################


########################
# SECURITY CONFIGURATION

# This needs to be filled out once we have a domain
# ALLOWED_HOSTS = []

# SECURITY CONFIGURATION
########################


########################
# DATABASE CONFIGURATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_setting('DATABASE_NAME', default='whats_next_db'),
        'USER': get_env_setting('DATABASE_USER'),
        'PASSWORD': get_env_setting('DATABASE_PASSWORD'),
        'HOST': get_env_setting('DATABASE_HOST', default='localhost'),
        'PORT': get_env_setting('DATABASE_PORT', default='5432'),
    }
}

# DATABASE CONFIGURATION
########################

