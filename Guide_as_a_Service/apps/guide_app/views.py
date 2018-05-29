from django.shortcuts import render,HttpResponse,redirect
from .models import *
import bcrypt
from django.contrib import messages


def guide_profile_page(request):
    return render(request,"guide_app/guidesucess.html")

# def guidesucess(request):
#     return render(request,"/guidesucess.html")

def update_profile_page_display(request):
    return render(request,"guide_app/update_profile.html")
