from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

import flights

# Create your views here.

from .models import Flight, Passenger


def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'index.html', context)


def flight(request, pk):
    flight = Flight.objects.get(id=pk)
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, 'flight.html', context)


def book(request, pk):
    if request.method == 'POST':
        flight = Flight.objects.get(id=pk)
        passenger = Passenger.objects.get(id=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return redirect(reverse('flight', args=(flight.id,)))
