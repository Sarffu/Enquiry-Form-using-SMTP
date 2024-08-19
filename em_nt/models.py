from django.db import models
from django.utils import timezone


class Signals(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
