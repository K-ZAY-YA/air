from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages

def traveller(request):
    travels = Traveller.objects.all() 
    return render(request, 'pages/Traveller.html', {'travels': travels})
def airline(request):
    airlines = Airline.objects.all()
    return render(request, 'pages/airline.html', {'airlines': airlines})   
def risk(request):
    risks = Riskaction.objects.all()
    return render(request, 'pages/risk.html', {'risks': risks})
def crew(request):
    crews = Crew.objects.all()
    return render(request, 'pages/crew.html', {'crews': crews})
def journey(request):
    journeys = journeysearch.objects.all()
    return render(request, 'pages/journey.html', {'journeys': journeys})