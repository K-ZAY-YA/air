from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages

def createtraveller(request):
    return render(request, 'pages/travellercreate.html')

def travellerstore(request):
    travel = Traveller()
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
    messages.success(request, "Traveller Added Successfullt")
    return redirect('traveller')     

def createairline(request):
    return render(request, 'pages/airlinecreate.html')

def airlinestore(request):
    air = Airline()
    air.operating_date = request.POST.get('operating_date') 
    air.airline = request.POST.get('airline')
    air.airline_name = request.POST.get('airline_name')
    air.airline_no = request.POST.get('airline_no') 
    air.depature_port = request.POST.get('depature_port') 
    air.arrival_port = request.POST.get('arrival_port')
    air.depature_date_time = request.POST.get('depature_date_time') 
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.flight_status = request.POST.get('flight_status')
    air.delay_issue = request.POST.get('delay_issue')
    air.remarks = request.POST.get('remarks')
    air.save()
    messages.success(request, "Airline Added Successfully")
    return redirect('airline')

def createcrew(request):
    return render(request, 'pages/crewcreate.html')

def crewstore(request):
    crews = Crew()
    crews.flight = request.POST.get('flight')
    crews.service_status = request.POST.get('service_status')
    crews.name = request.POST.get('name')
    crews.depature_port = request.POST.get('departure_port')
    crews.arrival_port = request.POST.get('arrival_port')
    crews.depature_date_time = request.POST.get('departure_date_time')
    crews.arrival_date_time = request.POST.get('arrival_date_time')
    crews.save()  
    messages.success(request, "Crew Added Successfully")
    return redirect('crew')

def createjourney(request):
    return render(request, 'pages/jourenycreate.html')

def journeystore(request):
    journey = journeysearch()
    journey.no = request.POST.get('no') 
    journey.name = request.POST.get('name')
    journey.dob = request.POST.get('dob')
    journey.father = request.POST.get('father') 
    journey.passport = request.POST.get('passport')
    journey.gender = request.POST.get('gender') 
    journey.flightname = request.POST.get('flightname') 
    journey.sector = request.POST.get('sector') 
    journey.depature_date_time = request.POST.get('depature_date_time') 
    journey.arrival_date_time = request.POST.get('arrival_date_time')
    journey.risk_status = request.POST.get('risk_status') 
    journey.save()
    messages.success(request, "Journey Added Successfully")
    return redirect('journey')

def createrisk(requrst):
    return render(requrst, 'pages/riskcreate.html')

def riskstore(request):
    risk = Riskaction()
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
    messages.success(request, "RiskAction Added Successfully")
    return redirect('risk')