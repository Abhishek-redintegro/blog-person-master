from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.TextField()
    description = models.TextField()
    posted_by = models.TextField()
    posted_on = models.DateTimeField()
