from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class University:
    university_id = models.TextField()



class DefaultUser(models.Model):
    email = models.EmailField(max_length=254, unique=True, null=True)
    university_id = models.CharField
class Department:
    university_id= models.CharField
    department_Name= models.CharField(null=True, max_length=256)
    department_id = models.CharField
    # head_of_department= models.


class Staff:
    name = models.CharField(null=True, max_length=30)
    username = models.CharField(null=True, unique=True, max_length=254)
    email = models.EmailField(null=True, unique=True,  max_length=254)
    phone_number = models.IntegerField(null=True, unique=True, max_length=11)
    title = models.CharField(null=True, max_length=254)
    address =  models.CharField(null=True)
    department_id = models.CharField


class Student(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=60, null=True)
    Last_name = models.CharField(max_length=60, null=True)
    Username = models.CharField(max_length=100, unique=True, null=True)
    Phone = models.CharField(max_length=11, unique=True, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    address = models.CharField(null=True, max_length=500)
    department = models.CharField(null=True, max_length=500)
    CurrentLevel = models.CharField(null=True, max_length=3)





