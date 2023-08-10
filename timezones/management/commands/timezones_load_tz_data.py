"""
loading timezone data into DB
"""

# Standard Library
import datetime

# Third Party
import pytz

# Django
from django.core.management.base import BaseCommand

# AA Time Zones
from timezones.models import TimezoneData


def get_input(text):
    """
    Wrapped input to enable tz import
    """

    return input(text)


class Command(BaseCommand):
    """
    Import timezones
    """

    help = "Imports timezone data"

    def _import_timezone_data(self) -> None:
        """
        Import time zone data
        :return:
        """

        timezones_imported = 0
        timezones_updated = 0

        for timezone_name in pytz.common_timezones:
            if timezone_name == "UTC":
                break

            timezone_panel_id = timezone_name.replace("/", "-").lower()
            timezone_utc_offset = datetime.datetime.now(
                pytz.timezone(timezone_name)
            ).strftime("%z")

            timezone, created = TimezoneData.objects.update_or_create(
                timezone_name=timezone_name,
                panel_id=timezone_panel_id,
                defaults={"utc_offset": timezone_utc_offset},
            )

            if created:
                action = "Importing"
                timezones_imported += 1
            else:
                action = "Updating"
                timezones_updated += 1

            self.stdout.write(
                f"{action} timezone '{timezone.timezone_name}' "
                f"with UTC offset of '{timezone.utc_offset}' "
                f"and panel ID of '{timezone.panel_id}'"
            )

        self.stdout.write(
            f"Import/Update done with {timezones_imported} new timezones imported "
            f"and {timezones_updated} timezones updated because they were already "
            "in the DB."
        )

    def handle(self, *args, **options):  # pylint: disable=unused-argument
        """
        Ask before running ...
        :param args:
        :param options:
        """

        self.stdout.write(
            "Timezones will be imported. "
            "Previously imported timezones will not be replaced or overwritten."
        )

        user_input = get_input("Are you sure you want to proceed? (yes/no)?")

        if user_input == "yes":
            self.stdout.write("Starting import of time zones. Please stand by.")
            self._import_timezone_data()
            self.stdout.write(self.style.SUCCESS("Timezones Import complete!"))
        else:
            self.stdout.write(self.style.WARNING("Aborted."))
