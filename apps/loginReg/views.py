# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages #imports messages for errors

from .models import * #imports everything from models

def index(request):
    if "userid" in request.session:  # if a session id is present
        print "userid in session" #print in the terminal to tell me
        return render(request,'success.html')
    else:                           #if there is no user in session
        print "no user in session"  #print it in the terminal
        return render (request, 'index.html') #and take the person back to the homepage

def register(request): #never renders a page, it only processes the registration 
    errors = User.objects.validate(request.POST) #creates a variable and assigns the validate object to it, which contains everything in request.post
    if len(errors) > 0: #if there are any errors (which is determined in models)
        for error in errors: #for each error in the list of errors
            messages.error(request,error) #print messages of the error
        return redirect ('/')
    pwhash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) #hashing password and setting a variable for it
    newUser = User.objects.create(first=request.POST['first'], last=request.POST['last'], email= request.POST['email'], password = pwhash) #create a user out of the information passed in the registration form and set it to a variable of newUser
    request.session["userid"] = newUser.id  #set session id to newuser id
    request.session["first"] = newUser.first #set the first name attached to the session to the newUser's first name
    return redirect('/success')

def login(request): #never renders a page, it only processes the login 
    errors = User.objects.loginvalidate(request.POST) #setting a variable of errors equal to all of the errors gathered from the models page
    if len(errors) > 0: #if there are any errors present
        for error in errors:
            messages.error(request,error) #tell us with the messages function
        return redirect ('/')
    else:
        print "got here"
        user = User.objects.filter(email=request.POST['email'])[0]  #run query to filter for email equal to one in the databast. A list is returned. [0] calls that place in the list. Then you need to use key/value for dictionary
        request.session["userid"] = user.id #set session id to be the userid
        request.session["first"] = user.first 
        return redirect("/success")
    

def logout(request, methods='POST'):
    request.session.clear() #clears session
    return redirect('/')

def success(request):
    user = request.session["userid"] #gets the user from the database
    return render(request,'success.html')