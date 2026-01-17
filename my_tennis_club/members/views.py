from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member #db
from django.db.models import Q

def main(request):
    mydata = Member.objects.filter(firstname__startswith='i') #filter only one data, you can use values() to get all data
    template = loader.get_template("main.html")
    context = {
        'username': mydata,
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
    mydata = Member.objects.filter(Q(firstname='Aap') | Q(firstname='isra')).values() #this is common ways to make or to filter using Q expressions
    template = loader.get_template("template.html")
    context = {
        'mymembers' : mydata,
        'fruitA': ['banana', 'apple', 'mango'],
        'fruitB': ['banana', 'charry', 'grape']
    }
    return HttpResponse(template.render(context, request))
