"""
Application init
"""

# Standard Library
from importlib import metadata

# Django
from django.utils.translation import gettext_lazy as _

__version__ = metadata.version("aa-timezones")
__title__ = _("Time Zones")

del metadata
