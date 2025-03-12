"""
Constants
"""

# Standard Library
import os

PACKAGE_NAME = "timezones"
APP_BASE_DIR = os.path.join(os.path.dirname(__file__))
APP_STATIC_DIR = os.path.join(APP_BASE_DIR, "static", PACKAGE_NAME)

AA_TIMEZONE_DEFAULT_PANELS: list[dict[str, str | dict[str, str]]] = [
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
        "panel_name": "China / Shanghai",
        "timezone": {
            "timezone_name": "Asia/Shanghai",
            "panel_id": "asia-shanghai",
        },
    },
    {
        "panel_name": "Australia / Sydney",
        "timezone": {
            "timezone_name": "Australia/ACT",
            "panel_id": "australia-act",
        },
    },
]
