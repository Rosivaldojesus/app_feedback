from django.shortcuts import render
from django.views import generic

# Create your views here.

class CoreView(generic.TemplateView):
    template_name = 'core/index.html'

    

