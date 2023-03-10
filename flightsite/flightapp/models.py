from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name


class UserRoles(models.Model):
    role = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.role


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField(max_length=250)
    email = models.EmailField(max_length=30, unique=True)
    role = models.ForeignKey(UserRoles, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    credit_card = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

class AirlineCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flight(models.Model):
    airline_company = models.ForeignKey(AirlineCompany, on_delete=models.CASCADE, default='unknown')
    origin_country = models.ForeignKey(Country, related_name='departures', on_delete=models.CASCADE, default='unknown')
    destination_country = models.ForeignKey(Country, related_name='arrivals', on_delete=models.CASCADE, default='unknown')
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickets = models.IntegerField()


class Ticket(models.Model):
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)