from django.db import models


class Tickets(models.Model):
    """Search tickets with updated solution"""
    problem = models.TextField()
    solution = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Problem: %s' % self.problem


class History(models.Model):
    """Search tickets with updated solution"""
    problem = models.TextField()
    solution = models.TextField()
    confidence = models.CharField(max_length=5, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Problem: %s ' % self.problem
