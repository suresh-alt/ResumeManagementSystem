from django import forms
from django.core.mail import send_mail

from app.models import *
import random
from app.utils import SendTextMessage
from RMS.settings import EMAIL_HOST_USER

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_otp(self):
        mail=self.cleaned_data['email']
        cno=self.cleaned_data['contact']
        rno=random.randint(100000,999999)
        subhect='otp'
        message='Welcome to Resume Management Project Your otp is'+ str(rno)
        SendTextMessage(message,cno)
        send_mail(subhect,message,EMAIL_HOST_USER,(mail,))
        return rno
    class Meta:
        model=RegistrationModel
        exclude=('status',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields="__all__"