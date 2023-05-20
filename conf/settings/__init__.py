from split_settings.tools import include

settings = [
    "django.py",  # standard django settings
    "database.py",  # postgres
    "rest_framework.py",  # rest-framework settings
    "celery.py",  # celery settings
    "redis.py",  # redis settings
]

# Include settings:
include(*settings)
