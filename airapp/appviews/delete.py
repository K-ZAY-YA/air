from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages


def airlinedelete(request, pk):
    try:
        airline = Airline.objects.get(id=pk)
        airline.delete()
        messages.success(request, "Airline deleted Successfully")
    except Airline.DoesNotExist:
        messages.error(request, "Airline does not exist")
    return redirect('/pages/airline')

def travellerdelete(request, pk):
    try:
        travels = Traveller.objects.get(id=pk)
        travels.delete()
        messages.success(request, "Traveller Deleted Successfully")
    except Traveller.DoesNotExist:
        messages.error(request, "Traveller does not exist")
    return redirect('/pages/traveller')

def crewdelete(request, pk):
    try:
        crew = Crew.objects.get(id=pk)
        crew.delete()
        messages.success(request, "Crew deleted Successfully")
    except Crew.DoesNotExist:
        messages.error(request, "Crew does not exist")
    
    return redirect('/pages/crew')

def journeydelete(request, pk):
    try:
        journey = journeysearch.objects.get(id=pk)
        journey.delete()
        messages.success(request, "Journey deleted Successfully")
    except Crew.DoesNotExist:
        messages.error(request, "Journey does not exist")
    
    return redirect('/pages/journey')

def riskdelete(request, pk):
    try:
        risk = Riskaction.objects.get(id=pk)
        risk.delete()
        messages.success(request, 'Risk Deleted Successfully')
    except Riskaction.DoesNotExist:
        messages.error(request, "Risk does not exist")
    return redirect('/pages/risk')