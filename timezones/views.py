"""
The views
"""

# Django
from django.shortcuts import render

# AA Time Zones
from timezones import __title__
from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import Timezones


def index(request, timestamp: str = None):
    """
    Index view

    :param request:
    :param timestamp:
    :return:
    """

    timezones = (
        Timezones.objects.select_related("timezone")
        .filter(is_enabled=True)
        .order_by("panel_name")
    )

    if not timezones:
        timezones = AA_TIMEZONE_DEFAULT_PANELS

    context = {"title": __title__, "timezones": timezones, "timestamp": timestamp}

    return render(
        request=request, template_name="timezones/index.html", context=context
    )
