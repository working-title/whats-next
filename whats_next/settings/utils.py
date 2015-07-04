import ast
import os

from django.core.exceptions import ImproperlyConfigured

def get_env_setting(setting, default=None, error_msg=None):
    """
    Get the setting from the system environment variables
    or return an exception, unless a default value is provided

    :param setting: name of env var to get setting from
    :param default: default return value if env var is not set
    :return: value from environment variable or default value
    """
    try:
        return os.environ['WHATS_NEXT' + setting]
    except KeyError:

        # return the default if one exists
        if default is not None:
            return default

        # otherwise throw an exception letting the user know the setting must be set
        if error_msg is None:
            error_msg = "You need to set the %s variable in your configuration file. " \
                        "Alternatively you can manually set it as an environment variable. " % setting

        raise ImproperlyConfigured(error_msg)


def get_env_setting_multiline_list(*args, **kwargs):
    """
    Return a list with one item per line of the file, the default can be a list or a string.
    """

    value = get_env_setting(*args, **kwargs)

    if isinstance(value, basestring):
        value = value.split('')

    if isinstance(value, list):
        return value

    raise ImproperlyConfigured('{} ({}) was not a string or a list.'.format(value, type(value)))


def get_env_setting_dict(*args, **kwargs):
    """
    Return a dictionary.tThe default can be a string or a python dict.
    """

    value = get_env_setting(*args, **kwargs)
    if isinstance(value, basestring):
        value = ast.literal_eval(value)

    if isinstance(value, dict):
        return value

    raise ImproperlyConfigured('{} ({}) was not a string or a python dictionary.'.format(value, type(value)))


def str2bool(v):
    """
    Converts a string input into a boolean result.

    :param v: string input
    :return: true if in array below, false if not
    """
    # make sure the input is a string, sometimes actual booleans are passed into this method (i.e default values)
    v = str(v)
    return v.lower() in ("yes", "true", "t", "1", "ok")


def assert_django_settings_module_is_set():
    """
    Asserts that the DJANGO_SETTINGS_MODULE environment variable is set. Will raise an exception if it isn't and
    display a helpful message!
    """
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        raise Exception('The DJANGO_SETTINGS_MODULE environment variable needs to be set.'
                        ' Check the README.md')
