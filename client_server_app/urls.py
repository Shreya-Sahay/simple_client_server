from django.conf.urls import url
from django.urls import path
from client_server_app import views

urlpatterns = [
    path("",views.Users,name = "users"),
    path("service_provider/",views.Service_provider,name = 'service_provider'),
]