"""
App config
"""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# AA Time Zones
from timezones import __version__


class AaTimezonesConfig(AppConfig):
    """
    AaTimezonesConfig
    """

    name: str = "timezones"
    label: str = "timezones"
    verbose_name: str = _(f"Time Zones v{__version__}")
