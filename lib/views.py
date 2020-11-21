from django.shortcuts import render
from django.http import HttpResponseRedirect
from .import forms,models


def home_view(request):
    return render(request,'library/home.html')

def adminsignup_view(request):
    form=forms.AdminSignupForm()
    if request.method=='POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('adminlogin')
    return render(request,'library/adminsignup.html',{'form':form})
    return render(request,'library/admin')
# Create your views here.
