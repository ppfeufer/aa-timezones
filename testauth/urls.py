# Django
from django.conf.urls import include, url

# Alliance Auth
from allianceauth import urls

urlpatterns = [
    # Alliance Auth URLs
    url(r"", include(urls)),
]
