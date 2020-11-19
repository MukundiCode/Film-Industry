from django.db import models
from django.contrib.auth.models import User

#This is where the models for the database are defined, and the tables 
#are made. Note, if any changes are made to this code, run the following commands
#in cmd to update.
#1. python manage.py make migrations (not sure about the space there)
#2. python manage.py migrate
class company(models.Model):
    companyName = models.CharField(max_length=80)
    address = models.CharField(max_length=254)
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
    jobDate = models.DateField(null=True)

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