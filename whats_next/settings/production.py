from .base import *


#####################
# DEBUG CONFIGURATION

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_EMAIL = DEBUG

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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_setting('DATABASE_NAME', default='publons_db'),
        'USER': get_env_setting('DATABASE_USER'),
        'PASSWORD': get_env_setting('DATABASE_PASSWORD'),
        'HOST': get_env_setting('DATABASE_HOST', default='localhost'),
        'PORT': get_env_setting('DATABASE_PORT', default='5432'),
        'OPTIONS': {
            'autocommit': True,
        }
    }
}

# DATABASE CONFIGURATION
########################


#####################
# RAVEN CONFIGURATION

RAVEN_CONFIG = {
    'dsn': get_env_setting('RAVEN_DSN'),
}

# RAVEN CONFIGURATION
#####################


###################
# APP CONFIGURATION

# INSTALLED_APPS += ('compressor',)

# APP CONFIGURATION
###################


########################
# TEMPLATE CONFIGURATION

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',       # Templates in TEMPLATE_DIRS
        'django.template.loaders.app_directories.Loader',  # Templates in app_dir/templates/
    ]),
)

# TEMPLATE CONFIGURATION
#####################


########################
# HAYSTACK CONFIGURATION

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'search.backend.PublonsElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
        'INCLUDE_SPELLING': True
    },
}

# HAYSTACK CONFIGURATION
########################


############################################
# EXTERNAL AUTH/API/SECRET KEY CONFIGURATION

MANDRILL_API_KEY = get_env_setting('MANDRILL_API_KEY')

DJRILL_WEBHOOK_SECRET = get_env_setting('DJRILL_WEBHOOK_SECRET')

# EXTERNAL AUTH/API/SECRET KEY CONFIGURATION
############################################


################################
# EXTERNAL SERVICE CONFIGURATION

# make sure these are set on production
SLACK_WEB_HOOK_EVENT_TOKEN = get_env_setting('SLACK_WEB_HOOK_EVENT_TOKEN')
SLACK_WEB_HOOK_EVENT_URL = get_env_setting('SLACK_WEB_HOOK_EVENT_URL')

# EXTERNAL SERVICE CONFIGURATION
################################


#################################
# UPDATE SPIDER URL CONFIGURATION

PUBLONS_UPDATE_SPIDER_URLS = []

# Latest 200 on PeerJ
PUBLONS_UPDATE_SPIDER_URLS += map(lambda i: 'https://peerj.com/articles/index.json?page=%s' % i, range(1, 2))

# Latest 500 on F1000
PUBLONS_UPDATE_SPIDER_URLS += map(lambda i: 'https://f1000research.com/articles?tab=ALL&subjectArea=&subtopic=&show=100&page=%s' % i, range(1, 2))

# PUBLONS_UPDATE_SPIDER_URLS += ['http://journal.frontiersin.org/']

FRONTIERS_JOURNAL_CODES = [
    ('fnagi', 'Frontiers in Aging Neuroscience'),
    ('fnbeh', 'Frontiers in Behavioral Neuroscience'),
    ('fbioe', 'Frontiers in Bioengineering and Biotechnology'),
    ('fcell', 'Frontiers in Cell and Developmental Biology'),
    ('fcimb', 'Frontiers in Cellular and Infection Microbiology'),
    ('fncel', 'Frontiers in Cellular Neuroscience'),
    ('fchem', 'Frontiers in Chemistry'),
    ('fncom', 'Frontiers in Computational Neuroscience'),
    ('feart', 'Frontiers in Earth Science'),
    ('fevo', 'Frontiers in Ecology and Evolution'),
    ('fendo', 'Frontiers in Endocrinology'),
    ('fenrg', 'Frontiers in Energy Research'),
    ('fenvs', 'Frontiers in Environmental Science'),
    ('fnevo', 'Frontiers in Evolutionary Neuroscience'),
    ('fgene', 'Frontiers in Genetics'),
    ('fnhum', 'Frontiers in Human Neuroscience'),
    ('fimmu', 'Frontiers in Immunology'),
    ('fnint', 'Frontiers in Integrative Neuroscience'),
    ('fmars', 'Frontiers in Marine Science'),
    ('fmats', 'Frontiers in Materials'),
    ('fmed', 'Frontiers in Medicine'),
    ('fmicb', 'Frontiers in Microbiology'),
    ('fmolb', 'Frontiers in Molecular Biosciences'),
    ('fnmol', 'Frontiers in Molecular Neuroscience'),
    ('fncir', 'Frontiers in Neural Circuits'),
    ('fnana', 'Frontiers in Neuroanatomy'),
    ('fnene', 'Frontiers in Neuroenergetics'),
    ('fneng', 'Frontiers in Neuroengineering'),
    ('fninf', 'Frontiers in Neuroinformatics'),
    ('fneur', 'Frontiers in Neurology'),
    ('fnbot', 'Frontiers in Neurorobotics'),
    ('fnins', 'Frontiers in Neuroscience'),
    ('fnut', 'Frontiers in Nutrition'),
    ('fonc', 'Frontiers in Oncology'),
    ('fped', 'Frontiers in Pediatrics'),
    ('fphar', 'Frontiers in Pharmacology'),
    ('fphy', 'Frontiers in Physics'),
    ('fphys', 'Frontiers in Physiology'),
    ('fpls', 'Frontiers in Plant Science'),
    ('fpsyt', 'Frontiers in Psychiatry'),
    ('fpsyg', 'Frontiers in Psychology'),
    ('fpubh', 'Frontiers in Public Health'),
    ('frobt', 'Frontiers in Robotics and AI'),
    ('fsurg', 'Frontiers in Surgery'),
    ('fnsyn', 'Frontiers in Synaptic Neuroscience'),
    ('fnsys', 'Frontiers in Systems Neuroscience'),
]


# Scrape nothing now,
# Don't want auto scraper to run while initial scrape is done.
# FRONTIERS_JOURNAL_CODES = []

for code, name in FRONTIERS_JOURNAL_CODES:
    PUBLONS_UPDATE_SPIDER_URLS += [
        'http://journal.frontiersin.org/%s' % code
    ]

# UPDATE SPIDER URL CONFIGURATION
#################################


#####################
# SLACK CONFIGURATION

SLACK_BACKEND = 'event_logger.utils.slack.SlackBackend'

# SLACK CONFIGURATION
#####################


###########################
# ASSET CONFIGURATION

USE_ASSET_MANIFEST = True

# ASSET CONFIGURATION
###########################

############
# DOI FINDER

DOI_FINDER_BACKENDS = [
    'publon.utils.doi.finders.MendeleyAPIFinder',
    'publon.utils.doi.finders.CrossrefFinder']

# DOI FINDER
############

##########
# Sessions

# Configure production to use the cache (redis) for sessions.
# Use the write through cache for the next two weeks to avoid any issues transferring where we would loose the
# tracking guids or logged in users. Two weeks from now (24/06/2015) we should be able to switch to the redis only
# cache. https://docs.djangoproject.com/en/1.8/topics/http/sessions/#using-cached-sessions

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'redis'

# Sessions
##########
