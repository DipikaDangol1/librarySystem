from django.shortcuts import render

def home_view(request):
    return render(request,'library/home.html')
# Create your views here.
