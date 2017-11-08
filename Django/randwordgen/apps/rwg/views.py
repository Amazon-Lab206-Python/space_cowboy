# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, views

from django.utils.crypto import get_random_string(length=14)

# Create your views here.

def index(request):
    context = {
        'rword': #get_random_string
        # https://stackoverflow.com/questions/25943850/django-package-to-generate-random-alphanumeric-string
    }
    return render(request, 'rwg/index.html', context)