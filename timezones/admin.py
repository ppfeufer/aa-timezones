"""
Admin backend config
"""

# Django
from django.contrib import admin, messages
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

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

    @admin.display(description=_("Panel name"), ordering="panel_name")
    def _panel_name(self, obj):
        return obj.panel_name

    @admin.display(description=_("Time zone"), ordering="timezone__timezone_name")
    def _timezone(self, obj):
        return obj.timezone.timezone_name

    actions = ("mark_as_active", "mark_as_inactive")

    @admin.action(description=_("Activate selected timezones"))
    def mark_as_active(self, request, queryset):
        """
        Mark timezone as active
        :param request:
        :param queryset:
        """

        notifications_count = 0
        failed = 0

        for obj in queryset:
            try:
                with transaction.atomic():
                    obj.is_enabled = True
                    obj.save()

                    notifications_count += 1
            except Exception:  # pylint: disable=broad-exception-caught
                failed += 1

        messages.success(
            request,
            ngettext(
                singular="Activated {notifications_count} timezone",
                plural="Activated {notifications_count} timezones",
                number=notifications_count,
            ).format(notifications_count=notifications_count),
        )

        if failed:
            messages.error(
                request,
                ngettext(
                    singular="Failed to activate {failed} timezone",
                    plural="Failed to activate {failed} timezones",
                    number=failed,
                ).format(failed=failed),
            )

        if queryset.count() - failed > 0:
            messages.success(
                request,
                ngettext(
                    singular="Activated {notifications_count} timezone",
                    plural="Activated {notifications_count} timezones",
                    number=notifications_count,
                ).format(notifications_count=notifications_count),
            )

    @admin.action(description=_("Deactivate selected timezones"))
    def mark_as_inactive(self, request, queryset):
        """
        Mark timezone as inactive
        :param request:
        :param queryset:
        """

        notifications_count = 0
        failed = 0

        for obj in queryset:
            try:
                with transaction.atomic():
                    obj.is_enabled = False
                    obj.save()

                    notifications_count += 1
            except Exception:  # pylint: disable=broad-exception-caught
                failed += 1

        if failed:
            messages.error(
                request,
                ngettext(
                    singular="Failed to deactivate {failed} timezone",
                    plural="Failed to deactivate {failed} timezones",
                    number=failed,
                ).format(failed=failed),
            )

        if queryset.count() - failed > 0:
            messages.success(
                request,
                ngettext(
                    singular="Deactivated {notifications_count} timezone",
                    plural="Deactivated {notifications_count} timezones",
                    number=notifications_count,
                ).format(notifications_count=notifications_count),
            )
