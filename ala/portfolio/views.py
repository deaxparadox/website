from django.shortcuts import render
from django.views import generic

class Portfolio(generic.TemplateView):
    template_name = 'portfolio/index.html'