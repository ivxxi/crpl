from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request, 'landingpage/land-page.html')


@login_required(login_url='/accounts/register/')
def pprofile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/register/')
def pdestination(request):
    return render(request, 'destination.html')



@login_required(login_url='/accounts/register/')
def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'registration/login.html')

def logout(request):
        logout(request)
        return redirect(request, 'registration/logout.html')
