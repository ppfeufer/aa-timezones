from django.db import models


# Create your models here.

class AaTimezones(models.Model):
    """Meta model for app permissions"""

    class Meta:
        managed = False
        default_permissions = ()
        permissions = (
            ('basic_access', 'Can access this app'),
        )
