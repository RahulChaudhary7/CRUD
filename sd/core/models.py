from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    standard = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)