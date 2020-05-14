from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('aa_timezones.basic_access')
def index(request):

    context = {
        'text': 'Hello, World!'
    }
    return render(request, 'aa_timezones/index.html', context)
