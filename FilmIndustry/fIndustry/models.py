from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class person(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE)
    firstName = models.CharField(max_length=80)
    surname = models.CharField(max_length=80, default="null")
    email = models.EmailField( max_length=254)
    phoneNumber = models.CharField(max_length=50)
class talent(models.Model):
    person = models.ForeignKey(person,null = True, on_delete = models.CASCADE)
    CHITNumber = models.IntegerField(max_length=4)
    gender = models.CharField(max_length = 254)
    address = models.CharField(max_length=254)
    race = models.CharField(max_length=20)

class bankDetails(models.Model):
    person = models.ForeignKey(person,null = True, on_delete = models.CASCADE)
    accountNumber = models.IntegerField(max_length=12)
    branchCode = models.IntegerField(max_length=12) 
    bankName = models.CharField(max_length=254)

class job(models.Model):
    ratePerHour = models.IntegerField(max_length=20)
    date = models.DateField

class jobTalent(models.Model):
    person = models.ForeignKey(person,null = True, on_delete = models.CASCADE)
    job = models.ForeignKey(job,null = True, on_delete = models.CASCADE)
    role = models.CharField(max_length=254)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)

class Admin(models.Model):
    adminID = models.CharField(max_length=12)

class CHITNumber(models.Model):
    CHITNo = models.IntegerField(default=0000)