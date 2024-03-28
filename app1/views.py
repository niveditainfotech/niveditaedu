from django.shortcuts import render,redirect
from .import models
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,"home.html")

def english(request):
    return render(request,"english.html")

def compotetive(request):
    return render(request,"compotetive.html")

def entrence(request):
    return render(request,"entrence.html")

def contactform(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        place=request.POST.get("place")
        course=request.POST["course"]

        models.Forms.objects.create(name=name,email=email,phone=phone,place=place,course=course).save()
        messages.success(request,"Submitted successfully..")
        return redirect("home")

def about(request):
    return render(request,"about.html")

def conatct(request):
    return render(request,"contacts.html")