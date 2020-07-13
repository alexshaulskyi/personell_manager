from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "works_for")
