from django.db import models

# Create your models here.
class Traveller(models.Model):
    flight = models.CharField(max_length=20, blank=False)
    timeframe = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    dob = models.DateField(blank=False) 
    nrc = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=6, blank=False)
    depature_port = models.CharField(max_length=10, blank=False)
    depature_date_time = models.DateTimeField(null=True)
    arrival_port = models.CharField(max_length=10, blank=False) 
    arrival_date_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, blank=True, null=True)


class Airline(models.Model):
    operating_date = models.DateTimeField(null=True)
    airline = models.CharField(max_length=20, blank=False)
    airline_name = models.CharField(max_length=20, blank=False)
    airline_no = models.IntegerField(blank=False, null=True)
    depature_port = models.CharField(max_length=10, blank=False)
    arrival_port = models.CharField(max_length=10, blank=False)
    depature_date_time = models.DateTimeField(null=True)
    arrival_date_time = models.DateTimeField(null=True)
    flight_status = models.CharField(max_length=10, blank=False)
    delay_issue = models.CharField(max_length=10, blank=False)
    remarks = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=10, blank=True, null=True)
    
class Riskaction(models.Model):
    no = models.IntegerField(5)
    name = models.CharField(max_length=20, blank=False)
    dob = models.DateField(blank=False) 
    father = models.CharField(max_length=20, blank=False)
    passport = models.IntegerField(10)
    gender = models.CharField(max_length=10, blank=False)
    nrc = models.CharField(max_length=50, blank=False)
    nationality = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=10, blank=True, null=True)

    
class Crew(models.Model):
    flight = models.CharField(max_length=20, blank=False)
    service_status = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=20, blank=False)
    depature_port = models.CharField(max_length=10, blank=False)
    arrival_port = models.CharField(max_length=10, blank=False) 
    depature_date_time = models.DateTimeField(null=True)
    arrival_date_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, blank=True, null=True)


class journeysearch(models.Model):
    no = models.IntegerField(5)
    name = models.CharField(max_length=20, blank=False)
    dob = models.DateField(blank=False) 
    father = models.CharField(max_length=20, blank=False)
    passport = models.IntegerField(10)
    gender = models.CharField(max_length=10, blank=False)
    flightname = models.CharField(max_length=20, blank=False, null=True)
    sector = models.CharField(max_length=10)
    depature_date_time = models.DateTimeField(null=True)
    arrival_date_time = models.DateTimeField(null=True)
    risk_status = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=10, blank=True, null=True)

    
    
