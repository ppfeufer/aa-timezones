"""
Test the apps' template tags
"""

# Django
from django.template import Context, Template
from django.test import TestCase, override_settings

# AA Time Zones
from timezones import __version__
from timezones.constants import PACKAGE_NAME
from timezones.helper.static_files import calculate_integrity_hash


class TestVersionedStatic(TestCase):
    """
    Test timezones_static template tag
    """

    @override_settings(DEBUG=False)
    def test_versioned_static_without_debug_enabled(self) -> None:
        """
        Test versioned static template tag without DEBUG enabled

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load timezones %}"
                "{% timezones_static 'css/timezones.min.css' %}"
                "{% timezones_static 'js/timezones.min.js' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = (
            f'/static/{PACKAGE_NAME}/css/timezones.min.css?v={context["version"]}'
        )
        expected_static_css_src_integrity = calculate_integrity_hash(
            "css/timezones.min.css"
        )
        expected_static_js_src = (
            f'/static/{PACKAGE_NAME}/js/timezones.min.js?v={context["version"]}'
        )
        expected_static_js_src_integrity = calculate_integrity_hash(
            "js/timezones.min.js"
        )

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertIn(
            member=expected_static_css_src_integrity, container=rendered_template
        )
        self.assertIn(member=expected_static_js_src, container=rendered_template)
        self.assertIn(
            member=expected_static_js_src_integrity, container=rendered_template
        )

    @override_settings(DEBUG=True)
    def test_versioned_static_with_debug_enabled(self) -> None:
        """
        Test versioned static template tag with DEBUG enabled

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load timezones %}" "{% timezones_static 'css/timezones.min.css' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = (
            f'/static/{PACKAGE_NAME}/css/timezones.min.css?v={context["version"]}'
        )

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertNotIn(member="integrity=", container=rendered_template)

    @override_settings(DEBUG=False)
    def test_invalid_file_type(self) -> None:
        """
        Test should raise a ValueError for an invalid file type

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load timezones %}" "{% timezones_static 'invalid/invalid.txt' %}"
            )
        )

        with self.assertRaises(ValueError):
            template_to_render.render(context=context)
