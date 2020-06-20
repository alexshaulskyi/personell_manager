from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login

#После регистрации пользователя нужно создать объект размещения
class SignUp(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('property_create')

    def form_valid(self, form):
        form.instance.job_title = 'MG'
        return super().form_valid(form)
