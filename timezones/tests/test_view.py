"""
Test checks for access to timezones
"""

# Django
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

# AA Time Zones
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

        :return:
        :rtype:
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
        :rtype:
        """

        # given
        self.client.force_login(user=self.user_1002)

        # when
        res = self.client.get(path=reverse(viewname="timezones:index"))

        # then
        self.assertListEqual(
            list1=res.context["timezones"], list2=AA_TIMEZONE_DEFAULT_PANELS
        )

    def test_custom_timezones(self):
        """
        Test custom timezones

        :return:
        :rtype:
        """

        # given
        self.client.force_login(user=self.user_1002)

        timezone_info = TimezoneData.objects.create(
            timezone_name="Europe/Berlin", utc_offset="+0100", panel_id="europe-berlin"
        )

        Timezones.objects.create(
            panel_name="Europe/Berlin", is_enabled=1, timezone=timezone_info
        )

        # when
        res = self.client.get(path=reverse(viewname="timezones:index"))

        # then
        self.assertQuerySetEqual(
            res.context["timezones"], Timezones.objects.all(), transform=lambda x: x
        )
