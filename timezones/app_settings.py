from django.conf import settings
from .utils import clean_setting

# set default panels if none are set in local.py
AA_TIMEZONES_ADDITIONAL_PANELS = clean_setting(
    'AA_TIMEZONES_ADDITIONAL_PANELS', [
        {
            'timezoneName': 'US/Pacific',
            'panelTitle': 'US / Pacific',
            'panelId': 'us-pacific'
        },
        {
            'timezoneName': 'US/Mountain',
            'panelTitle': 'US / Mountain',
            'panelId': 'us-mountain'
        },
        {
            'timezoneName': 'US/Central',
            'panelTitle': 'US / Central',
            'panelId': 'us-central'
        },
        {
            'timezoneName': 'US/Eastern',
            'panelTitle': 'US / Eastern',
            'panelId': 'us-eastern'
        },
        {
            'timezoneName': 'Europe/London',
            'panelTitle': 'EU / Western',
            'panelId': 'eu-western'
        },
        {
            'timezoneName': 'Europe/Berlin',
            'panelTitle': 'EU / Central',
            'panelId': 'eu-central'
        },
        {
            'timezoneName': 'Europe/Istanbul',
            'panelTitle': 'EU / Eastern',
            'panelId': 'eu-eastern'
        },
        {
            'timezoneName': 'Europe/Moscow',
            'panelTitle': 'Russia / Moscow',
            'panelId': 'russia-moscow'
        },
        {
            'timezoneName': 'Asia/Shanghai',
            'panelTitle': 'Russia / Siberia & China / Shanghai',
            'panelId': 'asia-shanghai'
        },
        {
            'timezoneName': 'Australia/ACT',
            'panelTitle': 'Australia / Sydney',
            'panelId': 'australia-atc'
        }
    ]
)
