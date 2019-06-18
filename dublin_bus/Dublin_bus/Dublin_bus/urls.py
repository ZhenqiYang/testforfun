
from django.contrib import admin
from django.conf.urls import url,include



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Dublin_map/',include('Dublin_map.urls')),
    ]
