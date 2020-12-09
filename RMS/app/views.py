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


def checklogin(request):
    print("==========1==========")
    try:
        print("======2===========")

        res=RegistrationModel.objects.get(email=request.POST.get('t1'),password=request.POST.get('t2'))
        print("===========3==========")
        if res.status == 'pending':
            print("===========4=========")
            return render(request,"app/login.html",{"message":'sorry your registration is pending'})
        elif res.status == 'closed':
            print("============5=======")
            return render(request,"app/login.html",{"message":'sorry your account is closed'})
        print("=================6==========")
        request.session['contact']=res.contact
        request.session['name']=res.name
        return redirect('viewprofile')
    except RegistrationModel.DoesNotExist:
        print("===========7============")
        return render(request, "app/login.html",{"message":"invalid details"})


def viewprofile(request):
    return render(request,"app/viewprofile.html")


def logout(request):
    del request.session['contact']
    del request.session['name']
    return redirect('main')