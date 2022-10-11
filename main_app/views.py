from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Celebrity, Car
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['celebrities'] = Celebrity.objects.all()
        return context


class CelebrityDetail(DetailView):
    model = Celebrity
    template_name = "celebrity_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context