"""
App settings and checks
"""

# Django
from django.apps import apps

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Time Zones
from timezones import __title__
from timezones.helper.static_files import calculate_integrity_hash

logger = LoggerAddTag(my_logger=get_extension_logger(name=__name__), prefix=__title__)


def allianceauth_discordbot_active():
    """
    Check if allianceauth-discordbot is installed and active

    :return:
    """

    return apps.is_installed("aadiscordbot")


class IntegrityHash:
    """
    Integrity hashes for static files
    """

    logger.debug("Calculating integrity hashes for static files")

    # CSS
    CSS = {"timezones.min.css": calculate_integrity_hash("css/timezones.min.css")}

    # JavaScript
    JS = {"timezones.min.js": calculate_integrity_hash("js/timezones.min.js")}

    # External Libraries
    EXTERNAL_LIBS = {
        "jquery.timeago.min.js": calculate_integrity_hash(
            "libs/jquery-timeago/1.6.7/jquery.timeago.min.js"
        ),
        "moment-timezone-with-data-1970-2030.min.js": calculate_integrity_hash(
            "libs/moment-timezone/0.5.36/moment-timezone-with-data-1970-2030.min.js"
        ),
        "weather-icons.min.css": calculate_integrity_hash(
            "libs/weather-icons/2.0.10/css/weather-icons.min.css"
        ),
    }
