from django.shortcuts import render,HttpResponse,redirect
from .models import *
import bcrypt

from django.contrib import messages

def index(request):
    print("*********",request)
    return render(request,"login_app/login_index.html")


def signup_window(request):
    return render(request,"login_app/signupwindow.html")   

def register(request):
    if request.method == 'POST':
        print("request",request)
        result = User.objects.insertuser(request.POST)
    if 'user' in result:
        request.session['userid'] = result['user'].id
        return redirect('/sucess')
    else:
        for keys in result:
            messages.error(request, result[keys])
        return render(request,"login_app/signupwindow.html")
    return redirect('/sucess')


def login(request):
    if request.method == 'POST':
        result = User.objects.validate_login(request.POST)
    if 'user' in result:
        request.session['userid'] = result['user'].id
        return redirect('/sucess')
    else:
        for keys in result:
            messages.error(request,result[keys])
        return render(request,"login_app/signupwindow.html")
    return redirect('/sucess')

