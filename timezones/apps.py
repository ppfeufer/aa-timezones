# -*- coding: utf-8 -*-

"""
app config
"""

from django.apps import AppConfig

from . import __version__


class AaTimezonesConfig(AppConfig):
    """AaTimezonesConfig"""

    name = "timezones"
    label = "timezones"
    verbose_name = "AA Timezones v{}".format(__version__)
