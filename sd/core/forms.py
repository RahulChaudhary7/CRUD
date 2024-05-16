from django import forms
from .models import student
from django.core import validators

class StudentReg(forms.ModelForm):
    class Meta:
        model = student
        fields = ['id','name','email','standard','stream']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'standard' : forms.TextInput(attrs={'class':'form-control'}),
            'stream' : forms.TextInput(attrs={'class':'form-control'}),
        }