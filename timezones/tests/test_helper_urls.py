"""
Unit tests for the timezones.helper.urls helper.
"""

# Standard Library
from unittest.mock import patch

# AA Time Zones
from timezones.helper.urls import reverse_absolute
from timezones.tests import BaseTestCase


class TestReverseAbsolute(BaseTestCase):
    """
    Test reverse_absolute helper
    """

    @patch("timezones.helper.urls.reverse")
    def test_returns_absolute_url_for_valid_viewname(self, mock_reverse):
        """
        Test returns absolute URL for valid viewname

        :param mock_reverse:
        :type mock_reverse:
        :return:
        :rtype:
        """

        mock_reverse.return_value = "/mocked-path/"

        with self.settings(SITE_URL="https://example.com"):
            result = reverse_absolute("mock_view")

        self.assertEqual(result, "https://example.com/mocked-path/")

    @patch("timezones.helper.urls.reverse")
    def test_handles_none_args_correctly(self, mock_reverse):
        """
        Test handles None args correctly

        :param mock_reverse:
        :type mock_reverse:
        :return:
        :rtype:
        """

        mock_reverse.return_value = "/mocked-path/"

        with self.settings(SITE_URL="https://example.com"):
            result = reverse_absolute("mock_view", args=None)

        self.assertEqual(result, "https://example.com/mocked-path/")

    @patch("timezones.helper.urls.reverse")
    def test_includes_args_in_generated_url(self, mock_reverse):
        """
        Test includes args in generated URL

        :param mock_reverse:
        :type mock_reverse:
        :return:
        :rtype:
        """

        mock_reverse.return_value = "/mocked-path/123/"

        with self.settings(SITE_URL="https://example.com"):
            result = reverse_absolute("mock_view", args=[123])

        self.assertEqual(result, "https://example.com/mocked-path/123/")
