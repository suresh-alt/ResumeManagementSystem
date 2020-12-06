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