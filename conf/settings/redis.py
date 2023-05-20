# Redis config
from conf.settings.django import env

REDIS_HOST = env("REDIS_HOST", cast=str, default="127.0.0.1")
REDIS_PORT = env("REDIS_PORT", cast=str, default="6379")
