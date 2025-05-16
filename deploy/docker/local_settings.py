import os

FRONTEND_HOST = os.getenv('FRONTEND_HOST', 'http://localhost')
PORTAL_NAME = os.getenv('PORTAL_NAME', 'MediaCMS')
SECRET_KEY = os.getenv('SECRET_KEY')
REDIS_LOCATION = os.getenv('REDIS_LOCATION', 'redis://redis:6379/1')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('POSTGRES_NAME', 'mediacms'),
        "HOST": os.getenv('POSTGRES_HOST', 'db'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
        "USER": os.getenv('POSTGRES_USER', 'mediacms'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'mediacms'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = os.getenv('DEBUG', 'False') == 'True'

# pedtv customisations
# https://github.com/mediacms-io/mediacms/blob/main/docs/admins_docs.md#5-configuration

CAN_ADD_MEDIA = "advancedUser"

# Uploaded videos can only be seen by registered users
PORTAL_WORKFLOW = "private"

# Just hides the register button
REGISTER_ALLOWED = False

CAN_LIKE_MEDIA = False
CAN_DISLIKE_MEDIA = False
CAN_REPORT_MEDIA = False
CAN_SHARE_MEDIA = True

MEDIA_IS_REVIEWED = True

USERS_CAN_SELF_REGISTER = False

CAN_COMMENT = "advancedUser"

