"""
Test for the providers module.
"""

# Standard Library
import logging

# AA Time Zones
from timezones.providers import AppLogger
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
        app_logger = AppLogger(logger, "PREFIX")

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("This is a test message")

        self.assertIn("[PREFIX] This is a test message", log.output[0])

    def test_handles_empty_prefix(self):
        """
        Tests that the AppLogger handles an empty prefix correctly.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger, "")

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("Message without prefix")

        self.assertIn("Message without prefix", log.output[0])

    def test_handles_non_string_prefix(self):
        """
        Tests that the AppLogger handles a non-string prefix correctly.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger, 123)

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("Message with numeric prefix")

        self.assertIn("[123] Message with numeric prefix", log.output[0])

    def test_handles_special_characters_in_prefix(self):
        """
        Tests that the AppLogger handles special characters in the prefix correctly.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger, "!@#$%^&*()")

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("Message with special characters in prefix")

        self.assertIn(
            "[!@#$%^&*()] Message with special characters in prefix", log.output[0]
        )

    def test_handles_empty_message(self):
        """
        Tests that the AppLogger handles an empty log message correctly.

        :return:
        :rtype:
        """

        logger = logging.getLogger("test_logger")
        app_logger = AppLogger(logger, "PREFIX")

        with self.assertLogs("test_logger", level="INFO") as log:
            app_logger.info("")

        self.assertIn("[PREFIX] ", log.output[0])
