from django import forms
from fIndustry.models import person
from fIndustry.models import talent, bankDetails

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
        fields = ['bankName','accountNumber','branchCode']