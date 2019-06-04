from django.db import models

#RELATIONSHIP 1

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Order(models.Model):
    date = models.DateField()
    order_number = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')


#RELATIONSHIP 2

class Country(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length=255)

class Province(models.Model):
    name = models.CharField(max_length = 255)
    year_founded = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='provinces')

class City(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')

class Residence(models.Model):
    address = models.CharField(max_length=255)
    year_built = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='residences')

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='people')


#RELATIONSHIP 3

class Actor(models.Model):
    name = models.CharField(max_length=255)

class Director(models.Model):
    name = models.CharField(max_length=255)

class Play(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='plays')

class Role(models.Model):
    role_name = models.CharField(max_length=255)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='roles')

