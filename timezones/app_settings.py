"""
App settings and checks
"""

# Django
from django.apps import apps
from django.conf import settings


def allianceauth_discordbot_installed():
    """
    Check if allianceauth-discordbot is installed and active

    :return:
    """

    return apps.is_installed("aadiscordbot")


def debug_enabled() -> bool:
    """
    Check if DEBUG is enabled

    :return:
    :rtype:
    """

    return settings.DEBUG
