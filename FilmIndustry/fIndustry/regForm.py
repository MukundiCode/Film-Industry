from django import forms
from fIndustry.models import person

class personForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['firstName','surname','email','phoneNumber']