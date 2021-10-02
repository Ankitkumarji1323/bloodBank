from django.db import models
from roomBooking.models import Destination
from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests':dests})

def signup(request):
    return render(request, 'signup.html')