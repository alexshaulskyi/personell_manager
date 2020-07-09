from django import forms
from .models import Hotel, Cleaning, Room
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class AddEmployee(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "job_title")

class UpdateEmployee(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "job_title")

class CleaningCreate(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ('name', 'difficulty', 'frequency')

class RoomCreate(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('number', 'category', 'building')


