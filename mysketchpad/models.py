from django.db import models

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True)
    event_date = models.DateField()

    def __str__(self):
        return self.title
