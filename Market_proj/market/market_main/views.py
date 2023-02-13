from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import * 


class Homepage(ListView):
    template_name = "market_main/main.html"
    model = Product
    context_object_name = "products"
    
    