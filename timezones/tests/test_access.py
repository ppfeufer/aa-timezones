"""
Test checks for access to timezones
"""

# Standard Library
from http import HTTPStatus

# Django
from django.test import TestCase
from django.urls import reverse

# AA Time Zones
from timezones.tests.utils import create_fake_user


class TestAccess(TestCase):
    """
    Test module access
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users

        :return:
        :rtype:
        """

        super().setUpClass()

        # User
        cls.user_1001 = create_fake_user(
            character_id=1001, character_name="Peter Parker"
        )

        cls.html_menu = f"""
            <li class="d-flex flex-wrap m-2 p-2 pt-0 pb-0 mt-0 mb-0 me-0 pe-0">
                <i class="nav-link fa-regular fa-clock fa-fw fa-fw align-self-center me-3 active"></i>
                <a class="nav-link flex-fill align-self-center me-auto active" href="{reverse('timezones:index')}">
                    Time Zones
                </a>
            </li>
        """

        cls.header_nav_brand = """
            <div class="navbar-brand">Time Zones</div>
        """

    def test_access_to_index_for_logged_in_user(self):
        """
        Test should open the index view for logged-in user

        :return:
        :rtype:
        """

        self.client.force_login(user=self.user_1001)

        response = self.client.get(path=reverse(viewname="timezones:index"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertContains(response=response, text=self.html_menu, html=True)
        self.assertContains(response=response, text=self.header_nav_brand, html=True)

    def test_access_to_index_as_public_page(self):
        """
        Test should open the index view as public page

        :return:
        :rtype:
        """

        response = self.client.get(path=reverse(viewname="timezones:index"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertContains(response=response, text=self.header_nav_brand, html=True)
