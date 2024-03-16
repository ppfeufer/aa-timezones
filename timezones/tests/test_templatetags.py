"""
Tests for our template tags
"""

# Django
from django.template import Context, Template
from django.test import TestCase

# AA Time Zones
from timezones import __version__


class TestVersionedStatic(TestCase):
    """
    Test versioned static template tag
    """

    def test_versioned_static(self):
        """
        Test versioned static template tag

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            "{% load timezones %}"
            "{% timezones_static 'timezones/css/timezones.min.css' %}"
        )

        rendered_template = template_to_render.render(context)

        self.assertInHTML(
            needle=f'/static/timezones/css/timezones.min.css?v={context["version"]}',
            haystack=rendered_template,
        )
