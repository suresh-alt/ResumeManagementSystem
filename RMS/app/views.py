from django.shortcuts import render
from app.forms import *

# Create your views here.
def show(request):
    return render(request,'app/home.html')


def reg(request):
    rf=RegistrationForm(request.POST)
    if request.method== 'post':
        pass
    else:
        return render(request,"app/reg.html",{"form":rf})