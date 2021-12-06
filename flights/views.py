from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Flight


def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'index.html', context)


def flight(request, pk):
    flight = Flight.objects.get(id=pk)
    context = {
        'flight': flight
    }
    return render(request, 'flight.html', context)
