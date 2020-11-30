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

def adminclick_view(request):
    return render(request,'library/adminclick.html')
       
# Create your views here.
def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['wapka1503@gmail.com'], fail_silently = False)
            return render(request, 'library/contactussuccess.html')
    return render(request, 'library/contactus.html', {'form':sub})