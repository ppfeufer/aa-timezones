"""
Versioned static URLs to break browser caches when changing the app version
"""

# Django
from django.template.defaulttags import register
from django.templatetags.static import static

# AA Time Zones
from timezones import __version__
from timezones.app_settings import IntegrityHash


@register.simple_tag
def timezones_static(path: str) -> str:
    """
    Versioned static URL

    :param path: Path to the static file relative to the static folder
    :type path: str
    :return: Versioned static URL
    :rtype: str
    """

    static_url = static(path)
    versioned_url = static_url + "?v=" + __version__

    return versioned_url


@register.simple_tag
def timezones_static_integrity_hash(
    static_file_type: str, relative_file_path: str
) -> str:
    """
    Returns the integrity hash for a file

    :param static_file_type: The type of static file
    :type static_file_type: str
    :param relative_file_path: The file path relative to the `aa-timezones/timezones/static/timezones` folder
    :type relative_file_path: str
    :return: Integrity hash
    :rtype: str
    """

    if static_file_type == "css":
        return IntegrityHash.CSS.get(relative_file_path)

    if static_file_type == "js":
        return IntegrityHash.JS.get(relative_file_path)

    if static_file_type == "lib":
        return IntegrityHash.EXTERNAL_LIBS.get(relative_file_path)

    raise ValueError(f"Unsupported static file type: {static_file_type}")
