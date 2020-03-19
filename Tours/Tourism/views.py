from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Places


# Create your views here.
def home(request):

    dests = Places.objects.all()
    return render(request, 'Home.html', {'dests': dests})


def about_us(request):
    return render(request, 'about_us.html')
