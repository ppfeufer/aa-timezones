import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testauth.settings.local")

from django.conf import settings  # noqa

app = Celery("testauth")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings")
app.conf.ONCE = {"backend": "allianceauth.services.tasks.DjangoBackend", "settings": {}}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
