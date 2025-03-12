"""
Tests for the auth_hooks module.
"""

# Standard Library
from unittest import TestCase
from unittest.mock import patch

# Django
from django.test import RequestFactory, modify_settings

# Alliance Auth
from allianceauth.services.hooks import MenuItemHook

# AA Time Zones
from timezones.auth_hooks import AaTimezonesMenuItem, register_menu, register_urls


class TestAaTimezonesMenuItem(TestCase):
    """
    Tests for the AaTimezonesMenuItem class
    """

    def setUp(self):
        """
        Set up

        :return:
        :rtype:
        """

        self.request = RequestFactory().get("/timezones")
        self.menu_item = AaTimezonesMenuItem()

    def test_render_calls_super(self):
        """
        Test render calls super

        :return:
        :rtype:
        """

        with patch.object(MenuItemHook, "render") as mock_super:
            self.menu_item.render(self.request)
            mock_super.assert_called_once_with(self.menu_item, self.request)


class TestRegisterMenu(TestCase):
    """
    Tests for the register_menu function
    """

    def test_returns_instance_of_AaTimezonesMenuItem(self):
        """
        Test returns instance of AaTimezonesMenuItem

        :return:
        :rtype:
        """

        result = register_menu()
        self.assertIsInstance(result, AaTimezonesMenuItem)


class TestRegisterUrls(TestCase):
    """
    Tests for the register_urls function
    """

    def test_returns_UrlHook_with_correct_attributes(self):
        """
        Test returns UrlHook with correct attributes

        :return:
        :rtype:
        """

        result = register_urls()

        self.assertEqual(result.__class__.__name__, "UrlHook")
        self.assertEqual(result.include_pattern.pattern._regex, r"^timezones/")
        self.assertEqual(result.excluded_views, {"timezones.views.index"})


class TestRegisterCogs(TestCase):
    """
    Tests for the register_cogs function
    """

    @modify_settings(INSTALLED_APPS={"append": "aadiscordbot"})
    def test_register_cogs_true(self):
        """
        Test register_cogs returns the correct cogs when aadiscordbot is installed

        :return:
        :rtype:
        """

        # AA Time Zones
        from timezones.auth_hooks import register_cogs

        cogs = register_cogs()

        self.assertEqual(cogs, ["timezones.aadiscordbot.cogs.time"])
