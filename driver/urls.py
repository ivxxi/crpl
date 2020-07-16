from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^home',views.landing, name = 'landing'),
    url(r'^$',views.driver, name = 'drivers home page'),
    url(r'^profile',views.dprofile, name = 'driver profile page'),
    url(r'^destination',views.ddestination, name = 'driver pick destination page'),
    url(r'^about',views.about, name = 'about page for app'),
    url(r'', include('passenger.urls',)),
]