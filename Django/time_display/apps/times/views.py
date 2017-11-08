# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    context = {
        'ctime': datetime.datetime.now().strftime('%b %d, %Y %I:%m %p')
    }
    return render(request, 'times/index.html', context)