# -*- coding: utf-8 -*-

"""
the views
"""
from typing import Dict, List, Union

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from timezones.models import Timezones

from timezones import __title__


@login_required
@permission_required("timezones.basic_access")
def index(request, timestamp: int = None):
    """
    index view

    :param request:
    :param timestamp:
    :return:
    """

    AA_TIMEZONE_DEFAULT_PANELS: List[Dict[str, Union[str, Dict[str, str]]]] = [
        {
            "panel_name": "US / Pacific",
            "timezone": {
                "timezone_name": "US/Pacific",
                "panel_id": "us-pacific",
            },
        },
        {
            "panel_name": "US / Mountain",
            "timezone": {
                "timezone_name": "US/Mountain",
                "panel_id": "us-mountain",
            },
        },
        {
            "panel_name": "US / Central",
            "timezone": {
                "timezone_name": "US/Central",
                "panel_id": "us-central",
            },
        },
        {
            "panel_name": "US / Eastern",
            "timezone": {
                "timezone_name": "US/Eastern",
                "panel_id": "us-eastern",
            },
        },
        {
            "panel_name": "EU / Western",
            "timezone": {
                "timezone_name": "Europe/London",
                "panel_id": "eu-western",
            },
        },
        {
            "panel_name": "EU / Central",
            "timezone": {
                "timezone_name": "Europe/Berlin",
                "panel_id": "eu-central",
            },
        },
        {
            "panel_name": "EU / Eastern",
            "timezone": {
                "timezone_name": "Europe/Istanbul",
                "panel_id": "eu-eastern",
            },
        },
        {
            "panel_name": "Russia / Moscow",
            "timezone": {
                "timezone_name": "Europe/Moscow",
                "panel_id": "russia-moscow",
            },
        },
        {
            "panel_name": "Russia / Siberia & China / Shanghai",
            "timezone": {
                "timezone_name": "Asia/Shanghai",
                "panel_id": "asia-shanghai",
            },
        },
        {
            "panel_name": "Australia / Sydney",
            "timezone": {
                "timezone_name": "Australia/ACT",
                "panel_id": "australia-atc",
            },
        },
    ]

    try:
        timezones = Timezones.objects.filter(is_enabled=True).order_by("panel_name")
    except Timezones.DoesNotExist:
        timezones = None

    if not timezones:
        timezones = AA_TIMEZONE_DEFAULT_PANELS

    context = {"title": __title__, "timezones": timezones, "timestamp": timestamp}

    return render(request, "timezones/index.html", context)
