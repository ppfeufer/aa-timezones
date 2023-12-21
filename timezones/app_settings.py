"""
App settings and checks
"""

# Django
from django.apps import apps

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Time Zones
from timezones import __title__

logger = LoggerAddTag(my_logger=get_extension_logger(name=__name__), prefix=__title__)


def allianceauth_discordbot_active():
    """
    Check if allianceauth-discordbot is installed and active

    :return:
    """

    return apps.is_installed("aadiscordbot")
