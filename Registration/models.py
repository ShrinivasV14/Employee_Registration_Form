
from django.db import models





class Employee(models.Model):

    EmpRegNo = models.CharField(max_length=264)
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    City = models.CharField(max_length=264)
    Age = models.PositiveIntegerField()
    MobileNo = models.PositiveIntegerField()
    Email = models.EmailField(max_length=254)


# Create your models here.
