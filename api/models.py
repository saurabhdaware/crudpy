from django.db import models

# Create your models here.
class StaffUser(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    email = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=14)
    password = models.CharField(max_length=20)