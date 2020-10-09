# -*- coding: utf-8 -*-

"""
hooks to AA
"""

from django.utils.translation import ugettext_lazy as _

from timezones import urls, __title__

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook


class AaTimezonesMenuItem(MenuItemHook):  # pylint: disable=too-few-public-methods
    """ This class ensures only authorized users will see the menu entry """

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _(__title__),
            "far fa-clock fa-fw",
            "timezones:index",
            navactive=["timezones:index"],
        )

    def render(self, request):
        """
        only if the user has access to this app
        :param request:
        :return:
        """
        if request.user.has_perm("timezones.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """
    register our menu item
    :return:
    """
    return AaTimezonesMenuItem()


@hooks.register("url_hook")
def register_urls():
    """
    register our base url
    :return:
    """
    return UrlHook(urls, "timezones", r"^timezones/")
