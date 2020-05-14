from django.urls import path
from . import views


app_name = 'aa_timezones'

urlpatterns = [
    path('', views.index, name='index'),
]
