from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm
from dashboard.models import Hotel
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from slugify import Slugify


class SignUp(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.job_title = 'MG'

        property_id = form.cleaned_data['property_id']
        property_name = form.cleaned_data['works_for']
        c_slugify = Slugify(to_lower=True)
        property_slug = c_slugify(property_name)

        Hotel.objects.create(name=property_name, slug=property_slug, property_id=property_id)

        return super().form_valid(form)