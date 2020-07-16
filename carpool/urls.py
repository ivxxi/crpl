
from django.conf.urls import url,include
from django.contrib import admin
from passenger import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'accounts/', include('registration.backends.simple.urls')),
    url(r'admin/', admin.site.urls),
    url(r'', include('passenger.urls',)),
    url(r'', include('driver.urls')),   
]
