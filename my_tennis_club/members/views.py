from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member #db

def main(request):
    template = loader.get_template("main.html")
    context = {
        'username': 'Aap',
    }
    return HttpResponse(template.render(context, request))

def members(request):
    mymembers = Member.objects.all().values()
    templates = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(templates.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    mymember = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        mymember : 'mymember',
    }
    return HttpResponse(template.render(context, request))
