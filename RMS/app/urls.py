"""RMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from RMS import settings
from app import views

urlpatterns = [
    path('',views.show,name='main'),
    path('reg/',views.reg,name='reg'),
    path('savereg/',views.reg,name='savereg'),
    path('validateotp/',views.validateotp,name='validateotp'),
    path('checkotp/',views.checkotp,name='checkotp'),
    path('message',views.message,name='message'),

    path('login/',views.login,name='login'),
    path('checklogin/',views.checklogin,name='checklogin'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('logout/',views.logout,name='logout'),
    path('fp',views.fp,name='fp'),
    path('setp/',views.setp,name='setp'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('saveprofile/',views.saveprofile,name='saveprofile'),
    path('delprofile/',views.delprofile,name='delprofile'),
    path('dpc/',views.dpc,name='dpc'),
    path('aboutus/',views.aboutus,name='aboutus')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)