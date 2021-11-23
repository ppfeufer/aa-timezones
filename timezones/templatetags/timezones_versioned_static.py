"""
Versioned static URLs to break browser caches when changing the app version
"""

from django.template.defaulttags import register
from django.templatetags.static import static

from timezones import __version__


@register.simple_tag
def timezones_static(path: str) -> str:
    """
    Versioned static URL
    :param path:
    :type path:
    :return:
    :rtype:
    """

    static_url = static(path)
    versioned_url = static_url + "?v=" + __version__

    return versioned_url
