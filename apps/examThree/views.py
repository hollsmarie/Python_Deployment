# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.contrib import messages

from datetime import date, time, datetime

import datetime

from .models import *

from ..loginReg.models import User

from django.shortcuts import render, HttpResponse, redirect

def index(request ):
    currentUser = User.objects.get(id=request.session['userid']) 
    trips = currentUser.userFaves.all()
    othersTrips = Trip.objects.exclude(favorites=currentUser)
    context = {
        "trips" : trips,
        "othersTrips": othersTrips,
    }
    return render(request,'examThree/index.html', context)

def add(request):
    return render(request,'examThree/add.html')

def update(request):
    currentUser = User.objects.get(id=request.session['userid'])
    errors = Trip.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('examThree:add')
    else:  
       Trip.objects.create(description=request.POST["description"], destination=request.POST["destination"], startDate=request.POST["startDate"], endDate=request.POST["endDate"], userAdded = currentUser)
    return redirect(reverse('examThree:index'))

def show(request, id):
    trip = Trip.objects.get(id=id)
    context = {
        "trip": trip
    }
    return render(request,'examThree/show.html', context)


def addfave(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    fave = Trip.objects.get(id=id)
    fave.favorites.add(currentUser)
    fave.save()
    return redirect(reverse('examThree:index'))


def remove(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    fave = Trip.objects.get(id=id)
    fave.favorites.remove(currentUser)
    fave.save()
    return redirect(reverse('examThree:index'))