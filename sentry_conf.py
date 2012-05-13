#-*- coding: utf-8 -*-

import json
import os.path
from sentry.conf.server import *

with open("/home/dotcloud/environment.json") as f:
    env = json.load(f)

CONF_ROOT = os.path.dirname(__file__)

ADMINS = ()
SENTRY_ADMINS = ()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "template1",
        "USER": env["DOTCLOUD_DB_SQL_LOGIN"],
        "PASSWORD": env["DOTCLOUD_DB_SQL_PASSWORD"],
        "HOST": env["DOTCLOUD_DB_SQL_HOST"],
        "PORT": int(env["DOTCLOUD_DB_SQL_PORT"]),
        }
}

# Make this unique, and don't share it with anybody.
#SECRET_KEY = ""

INSTALLED_APPS += ('django.contrib.staticfiles',)
STATIC_ROOT = "/home/dotcloud/volatile/static"
STATIC_URL = "/_static/"

SENTRY_USE_QUEUE = True

# Mail server configuration (also see DotCloud email service docs)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

DEFAULT_FROM_EMAIL = "dotcloud@%s-%s-%s-%s" % (
    env["DOTCLOUD_PROJECT"],
    env["DOTCLOUD_ENVIRONMENT"],
    env["DOTCLOUD_SERVICE_NAME"],
    env["DOTCLOUD_SERVICE_ID"]
)
SERVER_EMAIL = DEFAULT_FROM_EMAIL
SENTRY_SERVER_EMAIL = SERVER_EMAIL
