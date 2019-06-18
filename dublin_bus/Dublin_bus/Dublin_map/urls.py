from django.conf.urls import url
from Dublin_map import views



urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^test$', views.static_test),
    url(r'^money$', views.static_money),
    url(r'^database$', views.database),
    url(r'^btitle$', views.btitle),
    url(r'^create$', views.create),
    url(r'^delete$', views.delete),
    url(r'^bus_stop$', views.bus_stop),
    url(r'^send_jason$', views.send_json),
    url(r'^send_jason1$', views.send_json1),

    # url(r'^areas$', views.areas),
]
