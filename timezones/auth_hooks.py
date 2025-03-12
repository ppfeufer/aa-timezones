"""
Hooks to AA
"""

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# AA Time Zones
from timezones import __title__, urls
from timezones.app_settings import allianceauth_discordbot_installed


class AaTimezonesMenuItem(MenuItemHook):  # pylint: disable=too-few-public-methods
    """
    This class ensures only authorized users will see the menu entry
    """

    def __init__(self):
        # Set up menu entry for sidebar
        MenuItemHook.__init__(
            self,
            __title__,
            "fa-regular fa-clock fa-fw",
            "timezones:index",
            navactive=["timezones:"],
        )

    def render(self, request):
        """
        Only if the user has access to this app
        :param request:
        :return:
        """

        return MenuItemHook.render(self, request)


@hooks.register("menu_item_hook")
def register_menu():
    """
    Register our menu item
    :return:
    """

    return AaTimezonesMenuItem()


@hooks.register("url_hook")
def register_urls():
    """
    Register our base url
    :return:
    """

    return UrlHook(
        urls=urls,
        namespace="timezones",
        base_url=r"^timezones/",
        excluded_views=["timezones.views.index"],
    )


# Only register the cog when aadiscordbot is installed
if allianceauth_discordbot_installed():

    @hooks.register("discord_cogs_hook")
    def register_cogs():
        """
        Registering our discord cog
        """

        return ["timezones.aadiscordbot.cogs.time"]
