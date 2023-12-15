from django.apps import AppConfig

class BaseConfig(AppConfig):
    DEFAULT_AUTO_FIELD_NAME = 'django.db.models.BigAutofield'
    name = 'base'