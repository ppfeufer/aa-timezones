"""
App urls config
"""

# Django
from django.urls import path

# AA Time Zones
from timezones import views

app_name: str = "timezones"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:timestamp>/", views.index, name="index"),
]
