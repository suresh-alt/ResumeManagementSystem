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

    try:
        res=RegistrationModel.objects.get(email=request.POST.get('t1'),password=request.POST.get('t2'))
        if res.status == 'pending':
             return render(request,"app/login.html",{"message":'sorry your registration is pending'})
        elif res.status == 'closed':

            return render(request,"app/login.html",{"message":'sorry your account is closed'})

        request.session['contact']=res.contact
        request.session['name']=res.name
        request.session['rno']=res.rno
        return redirect('viewprofile')
    except RegistrationModel.DoesNotExist:

        return render(request, "app/login.html",{"message":"invalid details"})


def viewprofile(request):

        try:


            res=request.session['rno']
            if res:
                res=ProfileModel.objects.get(person__rno=res)
                status=True
                return render(request, "app/viewprofile.html", {"status": status, 'data': res})
            else:
                status=False
                return render(request, "app/viewprofile.html", {"status": status})

        except ProfileModel.DoesNotExist:
            return render(request,'app/viewprofile.html')
        except KeyError:
            return render(request, 'app/viewprofile.html')



def logout(request):
    try:
        del request.session['contact']

        del request.session['name']
        del  request.session['rno']
        return redirect('main')
    except KeyError:
        return render(request, "app/login.html", {"message": "please login first"})


def fp(request):
    return render(request,'app/forgotpassword.html')


def setp(request):
    cno=request.POST.get('t1')
    np=request.POST.get('t2')
    try:
        res=RegistrationModel.objects.get(contact=cno)
        res.password=np
        res.save()
        return redirect('login')
    except RegistrationModel.DoesNotExist:
        return render(request, 'app/forgotpassword.html',{"message":'invalid contact number'})


def update_profile(request):
    return render(request,"app/update_profile.html",{"form":ProfileForm()})


def saveprofile(request):
    pff=ProfileForm(request.POST,request.FILES)
    if pff.is_valid():
        pff.save()
        return redirect('viewprofile')
    else:
        return render(request, "app/update_profile.html", {"form": pff})


def delprofile(request):

    try:
        rno = request.session['rno']
        res = ProfileModel.objects.get(person__rno=rno)
        if res:
            status = True
            return render(request, "app/delprofile.html", {"status": status, 'data': res})
        else:
            status = False
            return render(request, "app/delprofile.html", {"status": status})


    except ProfileModel.DoesNotExist:
        return render(request,'app/delprofile.html')
    except KeyError:
        return render(request, 'app/delprofile.html')


def dpc(request):
    pno=request.POST.get('t1')
    print(pno)
    ProfileModel.objects.get(pno=pno).delete()
    return redirect('viewprofile')


def aboutus(request):
    return render(request,'app/aboutus.html')