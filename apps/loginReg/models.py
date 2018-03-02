# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt

import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, postData): #declare a controller of validation for the registration checker and create an empty dictionary of errors. Checks for errors below
        errors = {}
        if len(postData['first']) < 2:
            errors["First name cannot be blank!"] = "First"
        if not NAME_REGEX.match(postData['first']):
            errors["First name contains invalid characters or spaces."] = "First"
        if not NAME_REGEX.match(postData['last']):
            errors["Last name contains invalid characters or spaces."] = "Last"
        if len(postData['last']) < 2:
            errors["Last name cannot be blank!"] = "Last"
        if len(postData['email']) < 2:
            errors["Email cannot be blank!"] = "Email"
        if (User.objects.filter(email=postData["email"])):
            errors["Email already in use"] = "Email"
        if not EMAIL_REGEX.match(postData['email']):
            errors["Invalid Email Address!"] = "Email"
        elif User.objects.filter(email = postData["email"]).count() > 0:
            errors["Email address already exists in database!"] = "Email"
        if len(postData['password']) < 8:
            errors["Password much be at least 8 characters long"] = "PasswordEmail"
        if (postData['password']) != (postData['confirm']):
            errors["Passwords must match."] = "Password"
        return errors

    def loginvalidate(self, postData): #declare a controller to check for errors in your login process
        errors = {}
        if User.objects.filter(email=postData["email"]): #if the email the user enters matches 
            currentUser = User.objects.get(email=postData["email"]) #creates a variable called current user and sets the object equal to it
            tempPW = currentUser.password #sets the temporary PW to be the CurrentUser's pw
            if not bcrypt.checkpw(postData["password"].encode(), tempPW.encode()): #encrypts the password 
                errors["Invalid password"] = "password."
        else: 
            errors["Email address does not exist in database."] = "Email"
        return errors



class User(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    objects = UserManager()


