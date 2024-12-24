import django
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
import os

from django.db import models

#Handeling Signup + Login + Logout
def handleSignup(request):
    """
    This function is for user signup.This method will register new customers. 
    User will get values from form and it will check if username or email is already registerted or not.
    Then it will create a user object and save it.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns home page
    """
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).count()==1:
            messages.warning(request, "This username already exists, Please Choose another!!!")
            return redirect('home')

        if len(username)>10:
            messages.warning(request, " Your username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created successfully!!!")
        return redirect('home')

    else:
        return HttpResponse("404-Not Found")   


def handleLogin(request):

    """
    This method will access those who signed up before .we have to provide username and password for login.
    The site can not be entered if the username or password is incorrect.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns home page
    :return: returns httpResponse
    
    """

    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In!!!")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials, Please try again :(")
            return redirect('home')

    else:
        return HttpResponse("404-Not Found") 


def handleLogout(request):
    """
    This function is for user logout.
    
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns login page
    """

    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')