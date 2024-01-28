"""
Test cases for the models of the timezones app.
"""

# Django
from django.test import TestCase

# AA Time Zones
from timezones.models import TimezoneData, Timezones


class TimezoneDataModelTests(TestCase):
    """
    Test cases for the TimezoneData model
    """

    def test_timezone_data_creation(self):
        """
        Test creating a timezone data object

        :return:
        :rtype:
        """

        timezone_data = TimezoneData.objects.create(
            timezone_name="UTC", utc_offset="+00:00", panel_id="utc-panel"
        )

        self.assertIsInstance(timezone_data, TimezoneData)
        self.assertEqual(timezone_data.__str__(), "UTC")


class TimezonesModelTests(TestCase):
    """
    Test cases for the Timezones model
    """

    def setUp(self):
        """
        Set up test cases

        :return:
        :rtype:
        """

        self.timezone_data = TimezoneData.objects.create(
            timezone_name="UTC", utc_offset="+00:00", panel_id="utc-panel"
        )

    def test_timezones_creation_with_enabled_status(self):
        """
        Test creating a timezone object with enabled status

        :return:
        :rtype:
        """

        timezone = Timezones.objects.create(
            panel_name="UTC Panel", timezone=self.timezone_data, is_enabled=True
        )

        self.assertIsInstance(timezone, Timezones)
        self.assertEqual(timezone.__str__(), "UTC Panel")
        self.assertTrue(timezone.is_enabled)

    def test_timezones_creation_with_disabled_status(self):
        """
        Test creating a timezone object with disabled status

        :return:
        :rtype:
        """

        timezone = Timezones.objects.create(
            panel_name="UTC Panel", timezone=self.timezone_data, is_enabled=False
        )

        self.assertIsInstance(timezone, Timezones)
        self.assertEqual(timezone.__str__(), "UTC Panel")
        self.assertFalse(timezone.is_enabled)
