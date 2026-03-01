"""
Helper functions for URLs.
"""

# Standard Library
from urllib.parse import urljoin

# Django
from django.conf import settings
from django.urls import reverse


def reverse_absolute(viewname: str, args: list | None = None) -> str:
    """
    Return absolute URL for a view name.

    Similar to Django's ``reverse()``, but returns an absolute URL.
    """

    return urljoin(base=settings.SITE_URL, url=reverse(viewname=viewname, args=args))
