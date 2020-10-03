# -*- coding: utf-8 -*-

"""
our models
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class AaTimezones(models.Model):
    """Meta model for app permissions"""

    class Meta:  # pylint: disable=too-few-public-methods
        """AaTimezones :: Meta"""

        managed = False
        default_permissions = ()
        permissions = (("basic_access", "Can access this app"),)


class TimezoneData(models.Model):
    """
    available timzones
    imported from pytz
    """

    timezone_name = models.CharField(
        max_length=255, blank=False, unique=True, help_text=_("Name of the timezone")
    )

    utc_offset = models.CharField(
        max_length=255,
        blank=False,
        unique=False,
        help_text=_("UTC offset of the timezone"),
    )

    panel_id = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        help_text=_("ID of the timezone panel in frontend"),
    )

    def __str__(self) -> str:
        return str(self.timezone_name)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        TimezoneData :: Meta
        """

        verbose_name = _("Timezone Data")
        verbose_name_plural = _("Timezone Data")
        default_permissions = ()


class Timezones(models.Model):
    """
    configured timezones to display
    """

    panel_name = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        help_text=_("Name of the timezone panel"),
    )

    timezone = models.ForeignKey(
        TimezoneData,
        on_delete=models.CASCADE,
        blank=False,
        help_text=_("Selected timezone"),
    )

    is_enabled = models.BooleanField(
        default=True,
        help_text=_("Whether this timezone is enabled or not"),
    )

    def __str__(self) -> str:
        return str(self.panel_name)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        TimezoneData :: Meta
        """

        verbose_name = _("Timezone")
        verbose_name_plural = _("Timezones")
        default_permissions = ()
