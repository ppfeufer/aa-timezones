# Django
from django.urls import include, re_path

# Alliance Auth
from allianceauth import urls

urlpatterns = [
    # Alliance Auth URLs
    re_path(r"", include(urls)),
]
