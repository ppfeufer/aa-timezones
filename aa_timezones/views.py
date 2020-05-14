from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from . import __title__


@login_required
@permission_required('aa_timezones.basic_access')
def index(request):

    context = {
        'title': __title__
    }
    return render(request, 'aa_timezones/index.html', context)
