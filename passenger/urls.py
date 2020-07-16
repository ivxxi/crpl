from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect


urlpatterns=[
    url(r'^login',views.login,name ='login'),
    url(r'^$',views.landing,name = 'landing'),
    url(r'^profile/',views.pprofile, name = 'passenger profile page'),
    url(r'^destination/',views.pdestination, name = 'passenger pick destination page'),
    url(r'^about/',views.about, name = 'about page for app'),
    url(r'^logout/',views.logout,name ='logout'),
    url(r'', include('driver.urls')),  

]