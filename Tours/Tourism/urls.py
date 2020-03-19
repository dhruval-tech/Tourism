from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'Home/', views.home),
    url(r'about_us/', views.about_us)
]