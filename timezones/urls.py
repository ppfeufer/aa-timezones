# -*- coding: utf-8 -*-

"""
page urls config
"""

from django.conf.urls import url

from timezones import views


app_name: str = "timezones"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^(?P<timestamp>[0-9]+)/$", views.index, name="index"),
]
