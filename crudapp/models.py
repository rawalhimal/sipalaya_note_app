from django.db import models

# Create your models here.
class Note(models.Model):
    task = models.TextField()
    is_completed = models.BooleanField(default=False)
    