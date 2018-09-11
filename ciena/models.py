from django.db import connection
from django.db import models
from django.db import transaction


class Tickets(models.Model):
    """Flexible timeseries statistics.

    These are typically BTS-reported values like channel load.  As such, we
    will keep the default on-delete 'cascade' behavior and delete these
    instances when the linked BTS is deleted.
    """
    subject = models.TextField()
    solution = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
