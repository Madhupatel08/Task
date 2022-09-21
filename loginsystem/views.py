from copyreg import constructor
from email import message
import re
from time import process_time_ns
from django.http import HttpResponseNotFound
from http.client import HTTPResponse
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,'home.html')

def signin(request):
    x = random.randint(1,9)
    y = random.randint(1,9)
    z = random.randint(1,3)
    ans = 0
    oprtr = '+'
    if z == 1:
        ans= x+y
    elif z == 2:
        ans = x-y
        oprtr = '-'
    elif z == 3:
        ans = x*y
        oprtr = '*'
    obj = {'x' : x, 'y' : y, 'z' : oprtr, 'answer':ans}
    if request.method == 'POST':
        for key, value in request.POST.items():
            print(f'Key: {key} Value: {value}')
        username = request.POST.get('username_')
        pass1 = request.POST.get('pass1_')
        print(username, pass1) 
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            # fname = user.first_name
            return HttpResponseNotFound("hello")

            # return render(request,'welcome',{'fname':fname})
        else:
            # message.error(request, "Bad Credentials!")
            print("GOT NO USER",username)
            return redirect('signin')
    
    print(obj)
    return render(request,'signin.html',obj)


def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        fname =  request.POST['fname']
        lname =  request.POST['lname']
        email =  request.POST['email']
        pass1 =  request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        return redirect('signin')

    return render(request,'signup.html')




def signout(request):
    logout(request)
    message.success(request,"Logged Out Successfully!")
    return redirect('home')

def welcome(request):
    user = request.user
    fname = user.first_name
    return render(request,'welcome', {'fname' : fname})