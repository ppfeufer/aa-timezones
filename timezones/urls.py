# -*- coding: utf-8 -*-
from django.urls import path
from . import views


APP_NAME = "timezones"

urlpatterns = [
    path("", views.index, name="index"),
]
