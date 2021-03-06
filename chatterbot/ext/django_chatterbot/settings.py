"""
Default ChatterBot settings for Django.
"""
from django.conf import settings
from chatterbot import constants


CHATTERBOT_SETTINGS = getattr(settings, 'CHATTERBOT', {})

CHATTERBOT_DEFAULTS = {
    'name': 'ChatterBot',
    'storage_adapter': 'chatterbot.storage.DjangoStorageAdapter',
    'input_adapter': 'chatterbot.input.VariableInputTypeAdapter',
    'output_adapter': 'chatterbot.output.OutputAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

CHATTERBOT = CHATTERBOT_DEFAULTS.copy()
CHATTERBOT.update(CHATTERBOT_SETTINGS)

SILENCED_SYSTEM_CHECKS = ['mysql.E001']