"""
Test checks for access to timezones
"""
# Standard Library
from unittest.mock import patch

# Django
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

# AA Time Zones
from timezones.app_settings import allianceauth_major_version, template_path
from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import TimezoneData, Timezones
from timezones.tests.utils import create_fake_user


class TestAccess(TestCase):
    """
    Test access to the views
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users
        """

        super().setUpClass()

        cls.group = Group.objects.create(name="Superhero")

        cls.user_1002 = create_fake_user(
            character_id=1002, character_name="Bruce Wayne"
        )

    def test_default_timezones(self):
        """
        Test default timezones
        :return:
        """

        # given
        self.client.force_login(self.user_1002)

        # when
        res = self.client.get(reverse("timezones:index"))

        # then
        self.assertListEqual(res.context["timezones"], AA_TIMEZONE_DEFAULT_PANELS)

    def test_custom_timezones(self):
        """
        Test custom timezones
        :return:
        """

        # given
        self.client.force_login(self.user_1002)

        timezone_info = TimezoneData.objects.create(
            timezone_name="Europe/Berlin", utc_offset="+0100", panel_id="europe-berlin"
        )

        Timezones.objects.create(
            panel_name="Europe/Berlin", is_enabled=1, timezone=timezone_info
        )

        # when
        res = self.client.get(reverse("timezones:index"))

        # then
        self.assertQuerysetEqual(
            res.context["timezones"], Timezones.objects.all(), transform=lambda x: x
        )

    def test_should_return_aa_major_version(self):
        """
        Test should return the major version of the installed AA instance

        :return:
        :rtype:
        """

        with patch(target="timezones.app_settings.allianceauth__version", new="4.0.0"):
            curren_aa_major_version = allianceauth_major_version()
            expected_aa_major_version = 4

            self.assertEqual(
                first=curren_aa_major_version, second=expected_aa_major_version
            )

    def test_should_return_template_path(self):
        """
        Test should return the template path

        :return:
        :rtype:
        """

        with patch(target="timezones.app_settings.allianceauth__version", new="4.0.0"):
            current_template_path = template_path()
            expected_template_path = "timezones"

            self.assertEqual(first=current_template_path, second=expected_template_path)

    def test_should_return_legacy_template_path(self):
        """
        Test should return the template path to the legacy templates

        :return:
        :rtype:
        """

        with patch(target="timezones.app_settings.allianceauth__version", new="3.7.1"):
            current_template_path = template_path()
            expected_template_path = "timezones/legacy_templates"

            self.assertEqual(first=current_template_path, second=expected_template_path)
