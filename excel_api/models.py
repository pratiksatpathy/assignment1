from django.db import models


# Create your models here.
class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel')
    
class MyModel(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    sub_type = models.CharField(max_length=10)
    bus_type = models.CharField(max_length=15)