from django import forms
from .import models

class AdminSignupForm(forms.ModelForm):
    class SignupForm:
        fields=['first_name','last_name','username','password']
