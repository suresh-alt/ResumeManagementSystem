from django.contrib import messages
from django.shortcuts import render,redirect
from app.forms import *


# Create your views here.
def show(request):
    return render(request,'app/home.html')


def reg(request):
    print("---------1------------")
    rf=RegistrationForm(request.POST)
    if request.method== 'POST':
        print('------------------3-----------')
        if rf.is_valid():
            print('-------------4----------------')
            rf.save()

            return redirect('validateotp')
        else:
            return render(request, "app/reg.html", {"form": rf})

    else:
        print("--------------2-----------")
        return render(request,"app/reg.html",{"form":rf})


def validateotp(request):
    return render(request,"app/validateotp.html")


def checkotp(request):
    try:
       result= RegistrationModel.objects.get(contact=request.POST.get('t2'),otp=request.POST.get('t1'))
       if result.status == 'pending':
           result.status = 'Approved'
           result.save()
           messages.success(request,'you are successfully regestered')
           return redirect('message')
       elif result.status == 'Approved':
           messages.success(request, 'your registration is already approved')
           return redirect('message')


    except RegistrationModel.DoesNotExist:
            return render(request,"app/validateotp.html",{"error":'invalid  details'})


def message(request):
    return render(request,"app/message.html")


def login(request):
    return render(request,"app/login.html")