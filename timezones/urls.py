"""
page urls config
"""

# Django
from django.conf.urls import url

# AA Time Zones
from timezones import views

app_name: str = "timezones"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^(?P<timestamp>[0-9]+)/$", views.index, name="index"),
]
