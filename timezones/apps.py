# -*- coding: utf-8 -*-

"""
app config
"""

from django.apps import AppConfig

from timezones import __version__


class AaTimezonesConfig(AppConfig):
    """
    AaTimezonesConfig
    """

    name: str = "timezones"
    label: str = "timezones"
    verbose_name: str = "Timezones v{}".format(__version__)
