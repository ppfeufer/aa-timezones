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


def add_empty_field(embed: Embed) -> None:
    """
    Adding an empty field to the embed.

    :param embed:
    :type embed:
    :return:
    :rtype:
    """

    embed.add_field(
        name="\u200b",
        value="\u200b",
        inline=True,
    )


def add_empty_line(embed: Embed) -> None:
    """
    Adding an empty line to the embed.

    :param embed:
    :type embed:
    :return:
    :rtype:
    """

    embed.add_field(
        name="\u200b",
        value="\u200b",
        inline=False,
    )


class Time(commands.Cog):
    """
    A series of Time tools
    """

    def __init__(self, bot):
        self.bot = bot

    @classmethod
    def show_timezones(cls) -> Embed:
        """
        Create and format the embed for Discord.

        :return:
        :rtype:
        """

        fmt_utc = "%H:%M:%S (UTC)\n%A %d. %b %Y"
        fmt = "%H:%M:%S (UTC %z)\n%A %d. %b %Y"
        utc_now = datetime.utcnow()
        utc_timestamp = utc_now.strftime("%s")

        embed = Embed(title="Time")
        embed.colour = Color.green()

        embed.add_field(
            name="Your Local Time",
            value=f"<t:{utc_timestamp}:T>\n<t:{utc_timestamp}:D>",
            inline=True,
        )

        embed.add_field(
            name="EVE time",
            value=utc_now.strftime(fmt_utc),
            inline=True,
        )

        add_empty_field(embed=embed)
        add_empty_line(embed=embed)

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

        add_empty_line(embed=embed)

        # Add url to the timezones module
        timezones_url = reverse_absolute("timezones:index")

        embed.add_field(
            name="Timezones Conversion",
            value=timezones_url,
            inline=False,
        )

        return embed

    @commands.slash_command(name="time", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def time(self, ctx):
        """
        Returns the EVE time, and the current time in various time zones.

        :param ctx:
        :type ctx:
        :return:
        :rtype:
        """

        return await ctx.respond(embed=self.show_timezones(), ephemeral=True)


def setup(bot):
    """
    Set up the cog
    :param bot:
    """

    # Unload the `time` extension from `aadiscordbot`, so we can load our own.
    if bot.get_cog("Time") is not None:
        bot.remove_cog("Time")

    # Load our `time` extension
    bot.add_cog(Time(bot))
