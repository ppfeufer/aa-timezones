# -*- coding: utf-8 -*-

"""
admin backend config
"""

from django.contrib import admin

# Register your models here.
from timezones.models import Timezones


@admin.register(Timezones)
class TimezonesAdmin(admin.ModelAdmin):
    """
    timezones admin
    configure timezones that should be displayed
    """

    list_display = ("_panel_name", "_timezone", "is_enabled")
    ordering = ("panel_name",)
    list_filter = ("is_enabled",)

    @classmethod
    def _panel_name(cls, obj):
        return obj.panel_name

    _panel_name.short_description = "Panel Name"
    _panel_name.admin_order_field = "panel_name"

    @classmethod
    def _timezone(cls, obj):
        return obj.timezone.timezone_name

    _timezone.short_description = "Timezone"
    _timezone.admin_order_field = "timezone__timezone_name"

    actions = (
        "mark_as_active",
        "mark_as_inactive",
    )

    def mark_as_active(self, request, queryset):
        """
        Mark fleet type as active
        :param request:
        :param queryset:
        """

        notifications_count = 0

        for obj in queryset:
            obj.is_enabled = True
            obj.save()

            notifications_count += 1

        self.message_user(
            request, "{} timezone(s) activated".format(notifications_count)
        )

    mark_as_active.short_description = "Activate selected timezone(s)"

    def mark_as_inactive(self, request, queryset):
        """
        Mark fleet type as inactive
        :param request:
        :param queryset:
        """

        notifications_count = 0

        for obj in queryset:
            obj.is_enabled = False
            obj.save()

            notifications_count += 1

        self.message_user(
            request, "{} timezone(s) deactivated".format(notifications_count)
        )

    mark_as_inactive.short_description = "Deactivate selected timezone(s)"
