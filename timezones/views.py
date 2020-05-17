from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from . import __title__

from .app_settings import (
    AA_TIMEZONES_ADDITIONAL_PANELS
)



@login_required
@permission_required('timezones.basic_access')

def index(request):
    context = {
        'title': __title__,
        'timezonePanelData': AA_TIMEZONES_ADDITIONAL_PANELS
    }

    return render(request, 'timezones/index.html', context)
