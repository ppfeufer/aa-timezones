from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from . import __title__


@login_required
@permission_required('timezones.basic_access')
def index(request):

    context = {
        'title': __title__,
        'timezonePanelData': [
            {
                'timezoneName': 'US/Pacific',
                'panelTitle': 'US / Pacific',
                'panelType': 'default',
                'panelId': 'us-pacific'
            },
            {
                'timezoneName': 'US/Mountain',
                'panelTitle': 'US / Mountain',
                'panelType': 'default',
                'panelId': 'us-mountain'
            },
            {
                'timezoneName': 'US/Central',
                'panelTitle': 'US / Central',
                'panelType': 'default',
                'panelId': 'us-central'
            },
            {
                'timezoneName': 'US/Eastern',
                'panelTitle': 'US / Eastern',
                'panelType': 'default',
                'panelId': 'us-eastern'
            },
            {
                'timezoneName': 'Europe/London',
                'panelTitle': 'EU / Western',
                'panelType': 'default',
                'panelId': 'eu-western'
            },
            {
                'timezoneName': 'Europe/Berlin',
                'panelTitle': 'EU / Central',
                'panelType': 'default',
                'panelId': 'eu-central'
            },
            {
                'timezoneName': 'Europe/Istanbul',
                'panelTitle': 'EU / Eastern',
                'panelType': 'default',
                'panelId': 'eu-eastern'
            },
            {
                'timezoneName': 'Europe/Moscow',
                'panelTitle': 'Russia / Moscow',
                'panelType': 'default',
                'panelId': 'russia-moscow'
            },
            {
                'timezoneName': 'Asia/Shanghai',
                'panelTitle': 'Russia / Siberia & China / Shanghai',
                'panelType': 'default',
                'panelId': 'asia-shanghai'
            },
            {
                'timezoneName': 'Australia/ACT',
                'panelTitle': 'Australia / Sydney',
                'panelType': 'default',
                'panelId': 'australia-atc'
            }
        ]
    }

    return render(request, 'timezones/index.html', context)
