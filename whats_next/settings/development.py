from .base import *

#####################
# DEBUG CONFIGURATION

DEBUG = str2bool(
    get_env_setting('DEBUG', error_msg='You need to set DEBUG in your configuration file while developing.'
                                       ' Or alternatively you could set it manually as an environment variable.'))

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


###################
# APP CONFIGURATION

INSTALLED_APPS += ('debug_toolbar',)

# APP CONFIGURATION
###################


#######################
# LOGGING CONFIGURATION

LOG_LEVEL = get_env_setting('LOG_LEVEL', default='DEBUG')

# LOGGING CONFIGURATION
#######################
