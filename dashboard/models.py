from django.db import models
from users.models import User

room_status = [
    ('Грязная', 'Грязная'),
    ('Чистая', 'Чистая'),
    ('Не беспокоить', 'Не беспокоить'),
    ('Горничная в номере', 'Горничная в номере')
]

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    property_id = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='buildings')
    property_id = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Cleaning(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.FloatField()
    frequency = models.IntegerField()
    property_id = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms', blank=True, null=True)
    number = models.IntegerField()
    category = models.CharField(max_length=50)
    cleaning_type = models.ForeignKey(Cleaning, on_delete=models.PROTECT, related_name='rooms', blank=True, null=True)
    maid = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='rooms', blank=True, null=True)
    status = models.CharField(max_length=18, choices=room_status, blank=True, null=True)
    checkin_date = models.DateField(null=True, blank=True, auto_now_add=False)
    checkout_date = models.DateField(null=True, blank=True, auto_now_add=False)
    property_id = models.CharField(max_length=48)