from django import forms
from app.models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        exclude=('otp',)