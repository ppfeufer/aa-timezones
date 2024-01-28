"""
Tests for the admin module.
"""

# Standard Library
from unittest.mock import Mock

# Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase

# AA Time Zones
from timezones.admin import TimezonesAdmin
from timezones.models import TimezoneData, Timezones


class TestTimezonesAdmin(TestCase):
    """
    TimezonesAdmin tests
    """

    def setUp(self):
        """
        Setup

        :return:
        :rtype:
        """

        self.user = User.objects.create_user(username="test", password="test")
        timezone_data = TimezoneData.objects.create(
            timezone_name="UTC", utc_offset="+00:00", panel_id="utc"
        )
        self.timezone = Timezones.objects.create(
            panel_name="test", timezone=timezone_data, is_enabled=True
        )
        self.admin = TimezonesAdmin(Timezones, admin.site)

    def test_should_display_correct_fields(self):
        """
        Test should display correct fields

        :return:
        :rtype:
        """

        self.assertEqual(
            self.admin.list_display, ("_panel_name", "_timezone", "is_enabled")
        )
        self.assertEqual(self.admin.ordering, ("panel_name",))
        self.assertEqual(self.admin.list_filter, ("is_enabled",))

    def test_should_return_correct_panel_name(self):
        """
        Test should return correct panel name

        :return:
        :rtype:
        """

        self.assertEqual(self.admin._panel_name(self.timezone), "test")

    def test_should_return_correct_timezone(self):
        """
        Test should return correct timezone

        :return:
        :rtype:
        """

        self.assertEqual(self.admin._timezone(self.timezone), "UTC")

    def test_should_mark_as_active(self):
        """
        Test should mark as active

        :return:
        :rtype:
        """

        self.timezone.is_enabled = False
        self.timezone.save()
        request = Mock()
        self.admin.mark_as_active(
            request, Timezones.objects.filter(id=self.timezone.id)
        )
        self.timezone.refresh_from_db()
        self.assertTrue(self.timezone.is_enabled)

    def test_should_mark_as_inactive(self):
        """
        Test should mark as inactive

        :return:
        :rtype:
        """

        self.timezone.is_enabled = True
        self.timezone.save()
        request = Mock()
        self.admin.mark_as_inactive(
            request, Timezones.objects.filter(id=self.timezone.id)
        )
        self.timezone.refresh_from_db()
        self.assertFalse(self.timezone.is_enabled)
