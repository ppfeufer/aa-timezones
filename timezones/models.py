# -*- coding: utf-8 -*-

"""
our models
"""

from django.db import models


# Create your models here.
class AaTimezones(models.Model):
    """Meta model for app permissions"""

    class Meta:
        """AaTimezones :: Meta"""

        managed = False
        default_permissions = ()
        permissions = (("basic_access", "Can access this app"),)
