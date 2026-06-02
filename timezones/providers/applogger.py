"""
AppLogger provider
"""

# Standard Library
import logging

# AA Time Zones
from timezones import __title__


class AppLogger(logging.LoggerAdapter):
    """
    Custom logger adapter that adds a prefix to log messages.

    Taken from the `allianceauth-app-utils` package.
    Credits to: Erik Kalkoken
    """

    def __init__(self, my_logger: logging.Logger):
        """
        Initializes the AppLogger with a logger and a prefix.

        :param my_logger: Logger instance
        :type my_logger: logging.Logger
        """

        super().__init__(my_logger, {})

        self.prefix = __title__

    def process(self, msg, kwargs):
        """
        Prepares the log message by adding the prefix.

        :param msg: Log message
        :type msg: str
        :param kwargs: Additional keyword arguments
        :type kwargs: dict
        :return: Prefixed log message and kwargs
        :rtype: tuple
        """

        return f"[{self.prefix}] {msg}", kwargs
