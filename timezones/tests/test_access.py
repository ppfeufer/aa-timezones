"""
Test checks for access to timezones
"""

from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

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

    def test_has_no_access(self):
        """
        Test that a user without access get a 302
        :return:
        """

        # given
        self.client.force_login(self.user_1001)

        # when
        res = self.client.get(reverse("timezones:index"))

        # then
        self.assertEqual(res.status_code, 302)

    def test_has_access(self):
        """
        Test that a user with access get to see it
        :return:
        """

        # given
        self.client.force_login(self.user_1002)

        # when
        res = self.client.get(reverse("timezones:index"))

        # then
        self.assertEqual(res.status_code, 200)
