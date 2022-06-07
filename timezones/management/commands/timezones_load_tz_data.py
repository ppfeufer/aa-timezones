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
        import time zone data
        :return:
        """

        timezones_imported = 0
        timezones_skipped = 0

        for timezone_name in pytz.common_timezones:
            if timezone_name == "UTC":
                break

            # Check if timezone is already in DB
            if TimezoneData.objects.filter(timezone_name=timezone_name).exists():
                self.stdout.write(
                    f"Timezone '{timezone_name}' already in DB, skipping ..."
                )

                timezones_skipped += 1
            else:
                timezone_utc_offset = (
                    pytz.timezone(timezone_name)
                    .localize(datetime.datetime(2011, 1, 1))
                    .strftime("%z")
                )

                timezone_panel_id = timezone_name.replace("/", "-").lower()

                timezonedata = TimezoneData()
                timezonedata.timezone_name = timezone_name
                timezonedata.utc_offset = timezone_utc_offset
                timezonedata.panel_id = timezone_panel_id
                timezonedata.save()

                self.stdout.write(
                    f"Importing timezone '{timezone_name}' "
                    f"with UTC offset of '{timezone_utc_offset}' "
                    f"and panel ID of '{timezone_panel_id}'"
                )

                timezones_imported += 1

        self.stdout.write(
            f"Import done with {timezones_imported} new timezones imported "
            f"and {timezones_skipped} timezones skipped because they were already "
            "in the DB."
        )

    def handle(self, *args, **options):
        """
        ask before running ...
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
