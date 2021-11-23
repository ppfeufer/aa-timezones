from django.template import Context, Template
from django.test import TestCase

from timezones import __version__


class TestVersionedStatic(TestCase):
    def test_versioned_static(self):
        """
        Test versioned static template tag
        :return:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            "{% load timezones_versioned_static %}"
            "{% timezones_static 'timezones/css/timezones.min.css' %}"
        )

        rendered_template = template_to_render.render(context)

        self.assertInHTML(
            f'/static/timezones/css/timezones.min.css?v={context["version"]}',
            rendered_template,
        )
