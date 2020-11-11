from django.db import models

# Create your models here.

class Person(models.Model):
    u_name = models.TextField()
    u_desc = models.TextField()
    u_phone_no = models.TextField()
    u_email = models.TextField()
    u_password = models.TextField()