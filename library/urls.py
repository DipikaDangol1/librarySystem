
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from lib import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls') ),
    path('',views.home_view),
    path('adminclick',views.adminclick_view),
    path('adminsignup', views.adminsignup_view),
    
    path('contactus', views.contactus_view),
    path('studentclick',views.studentclick_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/home.html')),
    path('afterlogin', views.afterlogin_view),
    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewissuedbookbystudent',views.viewissuedbookbystudent),
    path('viewstudent', views.viewstudent_view),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]
