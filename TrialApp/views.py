from django.shortcuts import render, HttpResponse
from datetime import datetime
from TrialApp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is About Page")
def services(request):
    return render(request,'services.html')

    # return HttpResponse("This is Services Page")
def contact(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       reason = request.POST.get('reason')
       contact = Contact(name=name, email=email, phone=phone, reason=reason, date=datetime.today())
       contact.save()
       messages.success(request, "Your message has been sent !")
    return render(request,'contact.html')

def park(request):
    return render(request,'park.html')


def link1(request):
    return render(request,'link1.html')

def link2(request):
    return render(request,'link2.html')

def link3(request):
    return render(request,'link3.html')

    # return HttpResponse("This is Contact Page")
