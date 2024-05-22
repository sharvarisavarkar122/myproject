from django.db import models

# Create your models here.

from django.db import models
# chat/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
