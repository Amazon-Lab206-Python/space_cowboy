# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# views is def your pages, doing (request) and render your templates


def index(request):
    return render(request, "survey/index.html")


def process(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['tries'] += 1
    return redirect('/result')


def result(request):
    return render(request, 'survey/result.html')


def go_back(request):
    return render(request, "survey/index.html")
