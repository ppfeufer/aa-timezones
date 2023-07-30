"""
Celery config
"""

# Standard Library
import os

# Third Party
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testauth.settings.local")

# Django
from django.conf import settings  # noqa: E402

app = Celery("testauth")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings")
app.conf.ONCE = {"backend": "allianceauth.services.tasks.DjangoBackend", "settings": {}}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
