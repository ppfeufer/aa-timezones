"""
the views
"""

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from timezones import __title__
from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS
from timezones.models import Timezones


@login_required
@permission_required("timezones.basic_access")
def index(request, timestamp: int = None):
    """
    index view

    :param request:
    :param timestamp:
    :return:
    """

    try:
        timezones = Timezones.objects.filter(is_enabled=True).order_by("panel_name")
    except Timezones.DoesNotExist:
        timezones = None

    if not timezones:
        timezones = AA_TIMEZONE_DEFAULT_PANELS

    context = {"title": __title__, "timezones": timezones, "timestamp": timestamp}

    return render(request, "timezones/index.html", context)
