from django.shortcuts import render,HttpResponse,redirect
from .models import *
import bcrypt
from django.contrib import messages

def index(request):
    return redirect("sucess")

def sucess(request):
    return render(request,"tourist_app/sucess.html")