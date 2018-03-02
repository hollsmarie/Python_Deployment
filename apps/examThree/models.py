# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import pytz

from django.utils import timezone

from time import strptime,strftime

from datetime import datetime, date, time

import datetime

from ..loginReg.models import User

class TripManager(models.Manager):
    def validate(self, postData):
        errors = {}
        now = timezone.now()
        currentDate = unicode(datetime.datetime.now().date())
        startDate = unicode(postData['startDate'])
        endDate = unicode(postData['endDate'])
        if len(postData['destination']) < 1:
            errors["Destination"] = "Destination name cannot be empty"
        if len(postData['description']) < 1:
            errors["Description"] = "Description cannot be empty"
        if len(str(postData["startDate"])) < 1:
            errors["Start Date"] = "Date cannot be empty"
        if len(str(postData["endDate"])) < 1:
            errors["End Date"] = "Date cannot be empty"
        if startDate < currentDate:
            errors["Start Date"] = "Time travel isn't real." 
        if endDate < startDate:
            errors["End Date"] = "Trip cannot end before it begins, party pooper!" 
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    endDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    favorites = models.ManyToManyField(User, related_name="userFaves")
    userAdded = models.ForeignKey(User, related_name="userAdds")
    objects = TripManager()