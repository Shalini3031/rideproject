from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        abstract = True

class Admin(Person):
    id = models.AutoField(primary_key=True)
    otp = models.IntegerField(null=True, blank=True) 

class Driver(Person):
    driver_id = models.AutoField(primary_key=True)
    driving_license_number = models.CharField(max_length=50)
#     otp = models.IntegerField(null=True, blank=True) 


