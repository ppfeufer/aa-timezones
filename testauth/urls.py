from django.conf.urls import include, url

from allianceauth import urls

urlpatterns = [
    # Alliance Auth URLs
    url(r"", include(urls)),
]
