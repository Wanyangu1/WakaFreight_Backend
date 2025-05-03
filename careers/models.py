# careers/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField  # Use JSONField if not using PostgreSQL

class JobOpening(models.Model):
    position = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    posted = models.DateField()
    description = models.TextField()
    requirements = models.JSONField()  # Use ArrayField if using PostgreSQL

    def __str__(self):
        return self.position
