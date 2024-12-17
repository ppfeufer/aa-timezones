"""
Helper functions for static integrity calculations
"""

# Standard Library
import base64
import hashlib
import os

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Time Zones
from timezones import __title__
from timezones.constants import AA_TIMEZONES_STATIC_DIR

logger = LoggerAddTag(my_logger=get_extension_logger(__name__), prefix=__title__)


def calculate_integrity_hash(relative_file_path: str) -> str:
    """
    Calculates the integrity hash for a given static file

    :param relative_file_path: The file path relative to the `aa-timezones/timezones/static/timezones` folder
    :type relative_file_path: str
    :return: The integrity hash
    :rtype: str
    """

    file_path = os.path.join(AA_TIMEZONES_STATIC_DIR, relative_file_path)

    logger.debug(f"Calculating integrity hash for file: {file_path}")

    with open(file=file_path, encoding="utf-8") as static_file:
        file_hash = hashlib.sha512()

        content = static_file.read()
        file_hash.update(content.encode("utf-8"))
        integrity_hash = f"sha512-{base64.b64encode(file_hash.digest()).decode()}"

    return integrity_hash
