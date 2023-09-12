from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from .forms import *
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
import os
import math
import random
import smtplib


# Create your views here.
def Signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please login First")
            return redirect('signin')
    return inner
decs=[Signin_required,never_cache]

class SignInView(FormView):
    template_name="signin.html"
    form_class=SignInForm
    # def get(self,request):
    #     form=SignInForm()
    #     return render(request,"signin.html",{'form':form})
    def post(self,request):
        fdata=SignInForm(data=request.POST)
        if fdata.is_valid():
            unam=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=unam,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successful!!!")
                return redirect('custhome')
            else:
                messages.error(request,"Login Failed!! Invalid Username or Password!!")
                return redirect('signin')
        return render(request,'signin.html',{"form":fdata})
    
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('signin')

                
    
class SignUpView(View):
    def get(self,request):
        form=SignUpForm()
        return render(request,"signup.html",{'form':form})
    def post(self,request):
        fdata=SignUpForm(data=request.POST)
        if fdata.is_valid():
            digits="0123456789"
            OTP=""
            for i in range(6):
                OTP+=digits[math.floor(random.random()*10)]
                otp=OTP + "is your OTP"
                msg=otp
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login("backpackerandco585@gmail.com","Python@123")
                emailid=fdata.cleaned_data.get('email')
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                a=request.POST.get('OneTP')
                if a==OTP:
                    fdata.save()
                    return redirect('signin')
                else:
                    return render(request,"signup.html",{'form':fdata})
        return render(request,"signup.html",{'form':fdata})

# class SignUpView(CreateView):
#     form_class=SignUpForm
#     template_name="signup.html"
#     success_url=reverse_lazy("signin")
#     def form_valid(self,form):
#         messages.success(self.request,"Registration Successful!!")
#         return super().form_valid(form)
        
