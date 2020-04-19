from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'Home/', views.home),
    url(r'about_us/', views.about_us),
    url(r'register/', views.register),
    url(r'Places/', views.places),
    url(r'Contact_us/', views.contact),
    url(r'login/', views.login, name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'mail/', views.mail)
]