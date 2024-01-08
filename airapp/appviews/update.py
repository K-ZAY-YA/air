from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages


def airlineedit(request, pk):
    airlines = Airline.objects.get(id=pk)
    return render(request, 'pages/airlineedit.html', {'airlines': airlines})

def airlineupdate(request, pk):
    if request.method == 'POST':
        try:
            airline = Airline.objects.get(id=pk)
            airline.operating_date = request.POST.get('operating_date')
            airline.airline = request.POST.get('airline')
            airline.airline_name = request.POST.get('airline_name')
            airline.airline_nO = request.POST.get('airline_no')
            airline.depature_port = request.POST.get('depature_port')
            airline.depature_date_time = request.POST.get('arrival_port')
            airline.arrival_date_time = request.POST.get('depature_date_time')
            airline.arrival_date_time = request.POST.get('arrival_date_time')
            airline.flight_status = request.POST.get('flight_status')
            airline.delay_issue = request.POST.get('delay_issue')
            airline.remarks = request.POST.get('remarks')
            airline.save()   
            messages.success(request, "Airline Updated Successfully")
        except Airline.DoesNotExist:
            messages.error(request, "Airline does not exist")
        return redirect('/pages/airline') 

def creweidt(request, pk):
    crews = Crew.objects.get(id=pk)
    return render(request, 'pages/crewedit.html', {'crews': crews})

def crewupdate(request, pk):
    if request.method == 'POST':
        try:
            crew = Crew.objects.get(pk=pk)
            crew.flight = request.POST.get('flight')
            crew.service_status = request.POST.get('service_status')
            crew.name = request.POST.get('name')
            crew.depature_port = request.POST.get('departure_port')
            crew.arrival_port = request.POST.get('arrival_port')
            crew.depature_date_time = request.POST.get('departure_date_time')
            crew.arrival_date_time = request.POST.get('arrival_date_time')
            crew.save()  
            messages.success(request, "Crew Updated Successfully")
        except Crew.DoesNotExist:
            messages.error(request, "Crew does not exist")
        return redirect('/pages/crew') 


def travelleredit(request, pk):
    travels = Traveller.objects.get(id=pk)
    return render(request, 'pages/travellerupdate.html', {'travels':travels})

def travellerupdate(request, pk):
    if request.method == 'POST':
        try:
            travel = Traveller.objects.get(id = pk)
            travel.flight = request.POST.get('flight')
            travel.timeframe = request.POST.get('timeframe')
            travel.name = request.POST.get('name')
            travel.dob = request.POST.get('dob')
            travel.nrc = request.POST.get('nrc')
            travel.gender = request.POST.get('gender')
            travel.depature_port = request.POST.get('depature_port')
            travel.depature_date_time = request.POST.get('depature_date_time')
            travel.arrival_port = request.POST.get('arrival_port')
            travel.arrival_date_time = request.POST.get('arrival_date_time')
            travel.save()
            messages.success(request, "Traveller Updated Successfully")
        except Traveller.DoesNotExist:
            messages.error(request, "Traveller does not exist")
        return redirect('/pages/traveller') 

def journeyedit(request, pk):
    journeys = journeysearch.objects.get(id=pk)
    return render(request, 'pages/jourenyedit.html', {'journeys':journeys})

def journeyupdate(request, pk):
    if request.method == 'POST':
        try:
            joureny = journeysearch(id=pk)
            joureny.no = request.POST.get('no')
            joureny.name = request.POST.get('name')
            joureny.dob = request.POST.get('dob')
            joureny.father = request.POST.get('father')
            joureny.passport = request.POST.get('passport')
            joureny.gender = request.POST.get('gender')
            joureny.flightname = request.POST.get('flightname')
            joureny.sector = request.POST.get('sector')
            joureny.depature_date_time = request.POST.get('depature_date_time')
            joureny.arrival_date_time = request.POST.get('arrival_date_time')
            joureny.risk_status = request.POST.get('risk_status')
            joureny.save()
            messages.success(request, "Journey Update Successfully")
        except journeysearch.DoesNotExist:
            messages.error(request, "Journey does not exist")
        return redirect('/pages/journey')

def riskedit(request, pk):
    risks = Riskaction.objects.get(id=pk)
    return render(request, 'pages/riskedit.html', {'risks':risks})

def riskupdate(request, pk):
    if request.method == 'POST':
        try:
            risk = Riskaction(id=pk)
            risk.no = request.POST.get('no')
            risk.name = request.POST.get('name')
            risk.dob = request.POST.get('dob')
            risk.father = request.POST.get('father')
            risk.passport = request.POST.get('passport')
            risk.gender = request.POST.get('gender')
            risk.nrc = request.POST.get('nrc')
            risk.nationality = request.POST.get('nationality')
            risk.status = request.POST.get('status')
            risk.save()
            messages.success(request, "Risk Update Successfully")
        except Riskaction.DoesNotExist:
            messages.error(request, "Riskaction does not exist")
        return redirect('/pages/risk')

