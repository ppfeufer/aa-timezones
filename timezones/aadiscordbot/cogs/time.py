"""
"Time" cog for `allianceauth-discordbot`
https://github.com/pvyParts/allianceauth-discordbot
"""

# Standard Library
from datetime import datetime

# Third Party
import pytz
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands

# Django
from django.conf import settings

# Alliance Auth (External Libs)
from app_utils.urls import reverse_absolute

# AA Time Zones
from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import Timezones


class Time(commands.Cog):
    """
    A series of Time tools
    """

    def __init__(self, bot):
        self.bot = bot

    @classmethod
    def show_timezones(cls, deprecated_command_used: bool = False) -> Embed:
        """
        Create and format the embed for Discord
        :param deprecated_command_used:
        :return:
        """

        fmt_utc = "%H:%M:%S (UTC)\n%A %d. %b %Y"
        fmt = "%H:%M:%S (UTC %z)\n%A %d. %b %Y"
        utc_now = datetime.utcnow()
        utc_timestamp = utc_now.strftime("%s")

        embed = Embed(title="Time")
        embed.colour = Color.green()

        def add_empty_field() -> None:
            """
            Adding an empty field to the embed
            :return:
            """

            embed.add_field(
                name="\u200b",
                value="\u200b",
                inline=True,
            )

        def add_empty_line() -> None:
            """
            Adding an empty line to the embed
            :return:
            """

            embed.add_field(
                name="\u200b",
                value="\u200b",
                inline=False,
            )

        embed.add_field(
            name="Your Local Time",
            value=f"<t:{utc_timestamp}:T>\n<t:{utc_timestamp}:D>",
            # value=f"<t:{utc_timestamp}:T>",
            inline=True,
        )

        embed.add_field(
            name="EVE Time",
            value=utc_now.strftime(fmt_utc),
            inline=True,
        )

        add_empty_field()
        add_empty_line()

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
                        utc_now.astimezone(
                            pytz.timezone(configured_timezone.timezone.timezone_name)
                        ).strftime(fmt)
                    ),
                    inline=True,
                )

        # Get default timezones from module
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

        add_empty_line()

        # Add url to the timezones module
        timezones_url = reverse_absolute("timezones:index")

        embed.add_field(
            name="Timezones Conversion",
            value=timezones_url,
            inline=False,
        )

        if deprecated_command_used:
            embed.add_field(
                name="Deprecation Warning",
                value=(
                    "You used the deprecated `!time` command, which will be removed in "
                    "the foreseeable future. Please use `/time` instead."
                ),
                inline=False,
            )

        return embed

    @commands.command(pass_context=True)
    async def time(self, ctx):
        """
        Returns the Eve time and the current time in various time zones
        """

        return await ctx.send(embed=self.show_timezones(deprecated_command_used=True))

    @commands.slash_command(name="time", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def time_slash(self, ctx):
        """
        Returns the Eve time and the current time in various time zones
        """

        return await ctx.respond(embed=self.show_timezones())


def setup(bot):
    """
    Set up the cog
    :param bot:
    """

    # Unload the `time` extension from `aadiscordbot`, so we can load our own
    if bot.get_cog("Time") is not None:
        bot.remove_cog("Time")

    # Load our `time` extension
    bot.add_cog(Time(bot))
