from django import forms
from app.models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_otp(self):
        otp=self.cleaned_data['otp']
        print(otp)
        return 1234
    class Meta:
        model=RegistrationModel
        exclude=('status',)