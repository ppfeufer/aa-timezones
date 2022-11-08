"""
Admin backend config
"""

# Django
from django.contrib import admin

# AA Time Zones
from timezones.models import Timezones


@admin.register(Timezones)
class TimezonesAdmin(admin.ModelAdmin):
    """
    timezones admin
    Configure timezones that should be displayed
    """

    list_display = ("_panel_name", "_timezone", "is_enabled")
    ordering = ("panel_name",)
    list_filter = ("is_enabled",)

    @admin.display(
        description="Panel Name",
        ordering="panel_name",
    )
    @classmethod
    def _panel_name(cls, obj):
        return obj.panel_name

    @admin.display(
        description="Timezone",
        ordering="timezone__timezone_name",
    )
    @classmethod
    def _timezone(cls, obj):
        return obj.timezone.timezone_name

    actions = (
        "mark_as_active",
        "mark_as_inactive",
    )

    @admin.action(description="Activate selected timezone(s)")
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

        self.message_user(request, f"{notifications_count} timezone(s) activated")

    @admin.action(description="Deactivate selected timezone(s)")
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

        self.message_user(request, f"{notifications_count} timezone(s) deactivated")
