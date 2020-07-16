from django.shortcuts import render

from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import login



def login(request):
    login(request, user)
    return render(request, "registration/registration_form.html")
 
def logout(request):
    return render(request, 'registration/registration_form.html')

def landing(request):
    return render(request, 'landingpage/land-page.html')


def dregistration(request):
    return render(request, 'landingpage/land-page.html')



@login_required(login_url='/accounts/register/')
def driver(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/register/')
def dprofile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/register/')
def ddestination(request):
    return render(request, 'destination.html')

def about(request):
    return render(request, 'about.html')
