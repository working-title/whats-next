from .base import *

#####################
# DEBUG CONFIGURATION

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# DEBUG CONFIGURATION
#####################


########################
# SECURITY CONFIGURATION

ALLOWED_HOSTS = ['localhost']

# Can create a range of ips using the following formula
if DEBUG:
    from fnmatch import fnmatch

    class GlobList(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt):
                    return True
            return False

    INTERNAL_IPS = GlobList(['127.0.0.1', '10.0.1.*', '10.0.2.*'])

# SECURITY CONFIGURATION
########################

#######################
# LOGGING CONFIGURATION

LOG_LEVEL = get_env_setting('LOG_LEVEL', default='DEBUG')

# LOGGING CONFIGURATION
#######################


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'whats_next',
        'USER': 'whats_next',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS += ('debug_toolbar',)