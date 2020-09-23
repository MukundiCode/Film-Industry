from django import forms
from fIndustry.models import person
from fIndustry.models import talent, bankDetails

class personForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['firstName','surname','email','phoneNumber']

class talentForm(forms.ModelForm):
    class Meta:
        model = talent
        fields = ['CHITNumber','gender','address','race']

class bankForm(forms.ModelForm):
    class Meta:
        model = bankDetails
        fields = ['CHITNumber','bankName','accountNumber','branchCode']