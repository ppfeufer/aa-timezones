# -*- coding: utf-8 -*-

"""
page urls config
"""

from django.urls import path
from . import views


app_name = "timezones"

urlpatterns = [
    path("", views.index, name="index"),
]
