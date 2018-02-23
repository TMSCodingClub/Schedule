from django.db import models

class Event:
    name = models.CharField(max_length=75)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
