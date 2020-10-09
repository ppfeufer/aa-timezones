# coding=utf-8

"""
loading timezone data into DB
"""

import datetime
import pytz

from django.core.management.base import BaseCommand
from timezones.models import TimezoneData


def get_input(text):
    """
    wrapped input to enable tz import
    """

    return input(text)


class Command(BaseCommand):
    help = "Imports timezone data"

    def _import_timezone_data(self) -> None:
        """
        import time zone data
        :return:
        """

        timezones_imported = 0
        timezones_skipped = 0

        for timezone_name in pytz.common_timezones:
            timezone_utc_offset = (
                pytz.timezone(timezone_name)
                .localize(datetime.datetime(2011, 1, 1))
                .strftime("%z")
            )

            if timezone_name == "UTC":
                break

            timezone_panel_id = timezone_name.replace("/", "-").lower()

            # check if timezone is already in DB
            timezone_in_db = False

            try:
                timezonedata = TimezoneData.objects.filter(timezone_name=timezone_name)

                if timezonedata:
                    timezone_in_db = True
            except TimezoneData.DoesNotExist:
                self.stdout.write(
                    "Something went wrong while connecting to the Database"
                )

            if timezone_in_db:
                self.stdout.write(
                    "Timezone '{tz_name}' already in DB, skipping".format(
                        tz_name=timezone_name
                    )
                )

                timezones_skipped += 1
            else:
                timezonedata = TimezoneData()

                timezonedata.timezone_name = timezone_name
                timezonedata.utc_offset = timezone_utc_offset
                timezonedata.panel_id = timezone_panel_id
                timezonedata.save()

                self.stdout.write(
                    "Importing timezone '{tz_name}' with UTC offset of '{tz_offset}' "
                    "and panel ID of '{tz_panel_id}'".format(
                        tz_name=timezone_name,
                        tz_offset=timezone_utc_offset,
                        tz_panel_id=timezone_panel_id,
                    )
                )

                timezones_imported += 1

        self.stdout.write(
            "Import done with {tz_imported} new timezones imported and {tz_skipped} "
            "timezones skipped because they were already in the DB:".format(
                tz_imported=timezones_imported,
                tz_skipped=timezones_skipped,
            )
        )

    def handle(self, *args, **options):
        """
        ask before running ...
        :param args:
        :param options:
        """

        self.stdout.write(
            "Timezones will be imported. "
            "Previously imported timezones will not be replaced or overwritten"
        )

        user_input = get_input("Are you sure you want to proceed? (yes/no)?")

        if user_input == "yes":
            self.stdout.write("Starting import of time zones. Please stand by.")
            self._import_timezone_data()
            self.stdout.write(self.style.SUCCESS("Timezones Import complete!"))
        else:
            self.stdout.write(self.style.WARNING("Aborted."))
