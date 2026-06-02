"""
Test for the providers module.
"""

# Standard Library
import logging

# AA Time Zones
from timezones import __title__
from timezones.providers.applogger import AppLogger
from timezones.tests import BaseTestCase


class TestAppLogger(BaseTestCase):
    """
    Test the AppLogger provider.
    """

    def test_adds_prefix_to_log_message(self):
        """
        Tests that the AppLogger correctly adds a prefix to log messages.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger)

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("This is a test message")

        self.assertIn(f"[{__title__}] This is a test message", log.output[0])

    def test_handles_empty_message(self):
        """
        Tests that the AppLogger handles an empty log message correctly.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger)

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("")

        self.assertIn(f"[{__title__}] ", log.output[0])
