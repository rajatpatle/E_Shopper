from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    ecity = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    esal = models.FloatField()
    edesignation = models.CharField(max_length=50)