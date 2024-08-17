from django.db import models

# Create your models here.

from unittest.util import _MAX_LENGTH
from django.db import models
import pandas as pd
from joblib import load
from django.conf import settings
import os


from django.conf import settings
import joblib








class MyModel3(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    recentedu= models.CharField(max_length=50)
    relatedexp= models.CharField(max_length=50)
    companies= models.CharField(max_length=10)

    licenseType = models.CharField(max_length=10)
    passdate = models.DateField()
    expdate = models.DateField()

    cpccard = models.CharField(max_length=10)
    totalcpc = models.CharField(max_length=10)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)
     
    def __str__(self):
        return self.name




class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    qualifications = models.TextField()

    def __str__(self):
        return self.name




    