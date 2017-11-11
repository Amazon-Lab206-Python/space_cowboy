# -*- coding: utf-8 -*-
from __future__ import unicode_literals
<<<<<<< HEAD
from django.shortcuts import render, redirect
from IPython import embed
from .models import Dojo

# Create your views here.

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, 'dojo_ninjas/index.html', context )

def dojo_create(request):
    print "in dojo create method"

#     postData ={
#         "city" : request.POST['city'],
#         "state" : request.POST['state']     
#     }

#     model_resp = Dojo.objects.dojos_city_must_not_be_blank_validation(postData)

#     print model_resp
#     if model_resp[0] == True: #the dojo was successfully created
#         print: 'dojo successfully created, I should add a flash message saying it was successful'
#     else:
#         print 'not successful'
#         messages.add_message(request, messages.INFO, 'not successful')
    return redirect("/") 

def form_process(request):
    if request.method == "POST":
#         city = request.POST['city']
#         print city
        return redirect("/")

# def user_id(request, id):
#     if request.session.get(id) == None:
#         req_ses = None
#     else:
#         req_ses = request.session[id]
#     context ={

#     }
#     return redirect('/')
=======

from django.shortcuts import render

# Create your views here.
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6
