from django import forms
from django.contrib.auth.models import User
from .import models

class AdminSignupForm(forms.ModelForm):
    class SignupForm:
        fields=['first_name','last_name','username','password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class ContactusForm(forms.Form):
    Name=forms.CharField(max_length=40)
    Email=forms.EmailField()
    Message=forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
