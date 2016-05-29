import raven as raven

import os
import os.path
import sys
import random
import string
import ConfigParser

# Base directories
HOME_DIR = os.path.abspath(os.path.expanduser('~'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Random secret - production is loaded from a file
SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits)
                     for _ in range(30))

# Debug locally only
DEBUG = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')
ALLOWED_HOSTS = [
    'localhost',
    'tools.wmflabs.org'
]

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'axes',
    'gargoyle',
    'nexus',
    'bootstrap3',
    'tastypie',
    'cbng_interface',
    'cbng_review',
    'cbng_report',
]

# Middleware
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'axes.middleware.FailedLoginMiddleware'
]

# Add toolbar in debug mode
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INTERNAL_IPS = ['127.0.0.1', '::1']
    '''
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    '''
else:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')

# Urls
ROOT_URLCONF = 'cbng_interface.urls'
STATIC_ROOT = os.path.join(BASE_DIR, 'cbng_interface', 'static')
STATIC_URL = '/cluebotng/static/'
NEXUS_MEDIA_PREFIX = '/cluebotng/nexus/media/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cbng_interface.context_processors.staging_site',
            ]
        },
    },
]

# Authentication
AUTHENTICATION_BACKENDS = (
    'cbng_interface.auth.MediaWikiOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/cluebotng/login/mediawiki'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/cluebotng/'

# Wsgi
WSGI_APPLICATION = 'cbng_interface.wsgi.application'

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's52585__interface',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    },
    'bot': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's52585__cb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
DATABASE_ROUTERS = ['cbng_interface.db_router.AppRouter']

# Localisation
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Tastypie stuff
TASTYPIE_DEFAULT_FORMATS = ['json']

# Raven stuff
RAVEN_CONFIG = {
    'release': raven.fetch_git_sha(BASE_DIR)
}

# Slightly dodgy hack
STAGING_SITE = (os.environ.get('USER', '') == 'tools.cluebotng')

# Load config file
CBNG_CFG_FILE = os.path.join(HOME_DIR, '.cbng.cnf')
if os.path.isfile(CBNG_CFG_FILE):
    cfg = ConfigParser.RawConfigParser()
    cfg.read(CBNG_CFG_FILE)

    if cfg.has_section('interface_mysql'):
        DATABASES['default']['USER'] = cfg.get('interface_mysql', 'user')
        DATABASES['default']['PASSWORD'] = cfg.get('interface_mysql', 'password')
        DATABASES['default']['NAME'] = cfg.get('interface_mysql', 'name')
        DATABASES['default']['HOST'] = cfg.get('interface_mysql', 'host')

    if cfg.has_section('bot_mysql'):
        DATABASES['bot']['USER'] = cfg.get('bot_mysql', 'user')
        DATABASES['bot']['PASSWORD'] = cfg.get('bot_mysql', 'password')
        DATABASES['bot']['NAME'] = cfg.get('bot_mysql', 'name')
        DATABASES['bot']['HOST'] = cfg.get('bot_mysql', 'host')

    if cfg.has_section('general'):
        SECRET_KEY = cfg.get('general', 'session_secret')

    if cfg.has_section('raven'):
        RAVEN_CONFIG['dsn'] = cfg.get('raven', 'dsn')

    if cfg.has_section('oauth'):
        SOCIAL_AUTH_MEDIAWIKI_KEY = cfg.get('oauth', 'consumer')
        SOCIAL_AUTH_MEDIAWIKI_SECRET = cfg.get('oauth', 'secret')

# Social auth db hacks
SOCIAL_AUTH_UID_LENGTH = 190
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 190
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 190
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 190
SOCIAL_AUTH_EMAIL_LENGTH = 190
