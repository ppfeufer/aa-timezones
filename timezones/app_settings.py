"""
App settings and checks
"""

# Standard Library
from re import RegexFlag

# Django
from django.apps import apps
from django.conf import settings

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Time Zones
from timezones import __title__

logger = LoggerAddTag(my_logger=get_extension_logger(name=__name__), prefix=__title__)


def allianceauth_discordbot_installed():
    """
    Check if allianceauth-discordbot is installed and active

    :return:
    """

    return apps.is_installed("aadiscordbot")


def debug_enabled() -> RegexFlag:
    """
    Check if DEBUG is enabled

    :return:
    :rtype:
    """

    return settings.DEBUG
