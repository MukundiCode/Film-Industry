from django import forms
from fIndustry.models import person
from fIndustry.models import talent, bankDetails, job

#Tinashe Mukundi Chitamba
#This script deals with forms. It takes the data inputed in a form and populates
#a specific model of the database

class personForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['firstName','surname','email','phoneNumber','user']

class talentForm(forms.ModelForm):
    class Meta:
        model = talent
        fields = ['CHITNumber','gender','address','race','person']
        
class bankForm(forms.ModelForm):
    class Meta:
        model = bankDetails
        fields = ['bankName','accountNumber','branchCode','person']

class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ['ratePerHour','jobDate']