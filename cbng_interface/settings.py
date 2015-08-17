import os
import os.path
import sys
import random
import string

# Base directories
HOME_DIR = os.path.abspath(os.path.expanduser('~'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Random secret - production is loaded from a file
SECRET_KEY = ''.join(
    random.choice(string.ascii_uppercase + string.digits) for _ in range(30))

# Security keys
OAUTH_CONSUMER = None
OAUTH_SECRET = None

# Debug locally only
DEBUG = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')
ALLOWED_HOSTS = []

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
]

# Add toolbar in debug mode
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INTERNAL_IPS = ['127.0.0.1', '::1']
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')

# Urls
ROOT_URLCONF = 'cbng_interface.urls'
STATIC_URL = '/static/'

# Templates
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

    'report': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's51109__cb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    },

    'enwiki': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'enwiki_p',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

# Load tool settings
if os.getenv('INSTANCEPROJECT') == 'tools':
    DATABASES['default']['HOST'] = 'tools-db'

CBNG_CFG_FILE = os.path.join(HOME_DIR, '.cbng.cnf')
if os.path.isfile(CBNG_CFG_FILE):
    cfg = ConfigParser.RawConfigParser()
    cfg.read(CBNG_CFG_FILE)

    DATABASES['default']['USER'] = cfg.get('interface_mysql', 'user')
    DATABASES['default']['PASSWORD'] = cfg.get('interface_mysql', 'password')
    DATABASES['default']['NAME'] = cfg.get('interface_mysql', 'name')
    DATABASES['report']['HOST'] = cfg.get('interface_mysql', 'host')

    DATABASES['report']['USER'] = cfg.get('report_mysql', 'user')
    DATABASES['report']['PASSWORD'] = cfg.get('report_mysql', 'password')
    DATABASES['report']['NAME'] = cfg.get('report_mysql', 'name')
    DATABASES['report']['HOST'] = cfg.get('report_mysql', 'host')

    SECRET_KEY = cfg.get('general', 'session_secret')

    OAUTH_CONSUMER = cfg.get('oauth', 'consumer')
    OAUTH_SECRET = cfg.get('oauth', 'secret')

# Localisation
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True