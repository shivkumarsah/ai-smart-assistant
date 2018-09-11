"""Register our models for use in the admin site."""

from django.contrib import admin
from ciena import models

admin.site.register(models.Tickets)
admin.site.register(models.History)