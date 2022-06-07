"""
App settings and checks
"""

# Django
from django.apps import apps


def allianceauth_discordbot_active():
    """
    Check if allianceauth-discordbot is installed and active
    :return:
    """

    return apps.is_installed("aadiscordbot")
