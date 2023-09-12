from typing import Any, Dict
from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignInForm(forms.Form):
    username=forms.CharField(max_length=100,widget=(forms.TextInput(attrs={"placeholder":"User name"})))
    password=forms.CharField(max_length=50,widget=(forms.PasswordInput(attrs={"placeholder":"Password"})))

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]