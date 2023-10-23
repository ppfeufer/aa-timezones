"""
Test checks for access to timezones
"""

# Standard Library
from http import HTTPStatus

# Django
from django.test import TestCase
from django.urls import reverse

# AA Time Zones
from timezones.tests.utils import create_fake_user, is_legacy_auth


class TestAccess(TestCase):
    """
    Test module access
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users
        """

        super().setUpClass()

        # User cannot access timezones
        cls.user_1001 = create_fake_user(
            character_id=1001, character_name="Peter Parker"
        )

        cls.html_menu = f"""
            <li class="d-flex flex-wrap m-2 p-2 pt-0 pb-0 mt-0 mb-0 me-0 pe-0">
                <i class="nav-link far fa-clock fa-fw fa-fw align-self-center me-3 active"></i>
                <a class="nav-link flex-fill align-self-center" href="{reverse('timezones:index')}">
                    Time Zones
                </a>
            </li>
        """

        cls.header = """
            <div class="aa-timezones-header">
                <h1 class="text-center">Time Zones</h1>
            </div>
        """

        cls.header_logged_in_user = """
            <div class="navbar-brand">Time Zones</div>
        """

        if is_legacy_auth:
            cls.html_menu = f"""
                        <li>
                            <a class="active" href="{reverse('timezones:index')}">
                                <i class="far fa-clock fa-fw"></i>
                                Time Zones
                            </a>
                        </li>
                    """

            cls.header = """
                        <div class="aa-timezones-header">
                            <h1 class="page-header text-center">Time Zones</h1>
                        </div>
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

        if is_legacy_auth():
            self.assertContains(response=response, text=self.header, html=True)
        else:
            self.assertContains(
                response=response, text=self.header_logged_in_user, html=True
            )

    def test_access_to_index_as_public_page(self):
        """
        Test should open the index view as public page

        :return:
        :rtype:
        """

        response = self.client.get(path=reverse(viewname="timezones:index"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertContains(response=response, text=self.header, html=True)
