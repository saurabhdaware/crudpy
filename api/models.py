from django.db import models

# Create your models here.
class StaffUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phonenum = models.IntegerField(default=91)
    password = models.CharField(max_length=20)