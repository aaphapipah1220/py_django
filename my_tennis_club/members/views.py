from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    templates = loader.get_template('myfirst.html')
    return HttpResponse(templates.render())

# Create your views here.
