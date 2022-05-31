from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class SignUpForm(forms.Form):
    class Meta:
       model = User
       fields = ['username','first_name', 'last_name','email']
        #fm= SignUpForm (initial={'name':'intance'} auto_id=False)
    username =forms.CharField()
    firstname =forms.CharField()
    lastname =forms.CharField()
    email =forms.EmailField()

