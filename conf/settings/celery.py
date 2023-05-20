# Celery config
from conf.settings.django import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL", cast=str, default="redis://localhost:6379")
CELERY_BROKER_TRANSPORT_VISIBILITY_TIMEOUT = env(
    "CELERY_BROKER_TRANSPORT_VISIBILITY_TIMEOUT", cast=int, default=3600
)
CELERY_RESULT_BACKEND = env(
    "CELERY_RESULT_BACKEND", cast=str, default="redis://localhost:6379"
)
CELERY_ACCEPT_CONTENT = env(
    "CELERY_ACCEPT_CONTENT", cast=list, default=["application/json"]
)
CELERY_TASK_SERIALIZER = env("CELERY_TASK_SERIALIZER", cast=str, default="json")
CELERY_RESULT_SERIALIZER = env("CELERY_RESULT_SERIALIZER", cast=str, default="json")
CELERY_IMPORTS = env("CELERY_IMPORTS", cast=list, default=["api.tasks"])
