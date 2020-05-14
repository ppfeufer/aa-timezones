from django.apps import AppConfig
from . import __version__


class AaTimezonesConfig(AppConfig):
    name = 'aa_timezones'
    label = 'aa_timezones'
    verbose_name = 'AA Timezones v{}'.format(__version__)
