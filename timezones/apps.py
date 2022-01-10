"""
app config
"""

# Django
from django.apps import AppConfig

# AA Time Zones
from timezones import __version__


class AaTimezonesConfig(AppConfig):
    """
    AaTimezonesConfig
    """

    name: str = "timezones"
    label: str = "timezones"
    verbose_name: str = f"Timezones v{__version__}"
