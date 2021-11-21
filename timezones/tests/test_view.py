"""
Test checks for access to timezones
"""

from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import TimezoneData, Timezones

from .utils import create_fake_user


class TestAccess(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users
        """

        super().setUpClass()

        cls.group = Group.objects.create(name="Superhero")

        # User cannot access timezones
        cls.user_1001 = create_fake_user(1001, "Peter Parker")

        # User can access timezones
        cls.user_1002 = create_fake_user(
            1002, "Bruce Wayne", permissions=["timezones.basic_access"]
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
