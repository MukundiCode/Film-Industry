from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField( max_length=254)
    phoneNumber = models.CharField(max_length=50)
class talent(models.Model):
    CHITNumber = models.IntegerField(max_length=4)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=254)
    race = models.CharField(max_length=20)

class bankDetails(models.Model):
    CHITNumber = models.IntegerField(max_length=4)
    accountNumber = models.IntegerField(max_length=12)
    branchCode = models.IntegerField(max_length=12) 
    bankName = models.CharField(max_length=254)

class job(models.Model):
    ratePerHour = models.IntegerField(max_length=20)
    date = models.DateField

class jobTalent(models.Model):
    role = models.CharField(max_length=254)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)

class Admin(models.Model):
    adminID = models.CharField(max_length=12)