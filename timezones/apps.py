"""
App config
"""

# Django
from django.apps import AppConfig
from django.utils.text import format_lazy

# AA Time Zones
from timezones import __title_translated__, __version__


class AaTimezonesConfig(AppConfig):
    """
    AaTimezonesConfig
    """

    name: str = "timezones"
    label: str = "timezones"
    verbose_name = format_lazy(
        "{app_title} v{version}", app_title=__title_translated__, version=__version__
    )
