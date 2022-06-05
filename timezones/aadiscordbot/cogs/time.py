"""
"Time" cog for allianceauth-discordbot - https://github.com/pvyParts/allianceauth-discordbot
"""

# Standard Library
from datetime import datetime

# Third Party
import pytz
from aadiscordbot.app_settings import get_site_url
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands

# Django
from django.conf import settings
from django.urls import reverse

# AA Time Zones
from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import Timezones


class Time(commands.Cog):
    """
    A series of Time tools
    """

    def __init__(self, bot):
        self.bot = bot

    def show_timezones(self):
        """
        Create and format the embed for Discord
        """

        fmt_utc = "%H:%M:%S (UTC)\n%A %d. %b %Y"
        fmt = "%H:%M:%S (UTC %z)\n%A %d. %b %Y"

        embed = Embed(title="Time")
        embed.colour = Color.green()

        embed.add_field(
            name="EVE Time",
            value=datetime.utcnow().strftime(fmt_utc),
            inline=False,
        )

        configured_timezones = (
            Timezones.objects.select_related("timezone")
            .filter(is_enabled=True)
            .order_by("panel_name")
        )

        # Get configured timezones from module setting
        if configured_timezones.count() > 0:
            for configured_timezone in configured_timezones:
                embed.add_field(
                    name=configured_timezone.panel_name,
                    value=(
                        datetime.utcnow()
                        .astimezone(
                            pytz.timezone(configured_timezone.timezone.timezone_name)
                        )
                        .strftime(fmt)
                    ),
                    inline=True,
                )

        # get default timezones from module
        else:
            configured_timezones = AA_TIMEZONE_DEFAULT_PANELS

            for configured_timezone in configured_timezones:
                embed.add_field(
                    name=configured_timezone["panel_name"],
                    value=(
                        datetime.utcnow()
                        .astimezone(
                            pytz.timezone(
                                configured_timezone["timezone"]["timezone_name"]
                            )
                        )
                        .strftime(fmt)
                    ),
                    inline=True,
                )

        # add url to the timezones module
        timezones_url = get_site_url() + reverse("timezones:index")

        embed.add_field(
            name="Timezones Conversion",
            value=timezones_url,
            inline=False,
        )

        return embed

    @commands.command(pass_context=True)
    async def time(self, ctx):
        """
        Returns the Eve time and the current time in various time zones
        """

        return await ctx.send(embed=self.show_timezones())

    @commands.slash_command(name="time", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def time_slash(self, ctx):
        """
        Returns the Eve time and the current time in various time zones
        """

        return await ctx.respond(embed=self.show_timezones())


def setup(bot):
    """
    Setup the cog
    :param bot:
    """

    # Unload the `time` extemsion from `aadiscordbot`, so we can load our own
    if bot.get_cog("Time") is not None:
        bot.remove_cog("Time")

    # Load our `time` extension
    bot.add_cog(Time(bot))
