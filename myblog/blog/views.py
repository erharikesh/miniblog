from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout 
# Create your views here
#home
def home(request):
    return render(request, 'blog\home.html')
def about(request):
  return render(request, 'blog/about.html') 
def contact(request):
  return render(request, 'blog/contact.html')
def dashboard(request):
    return render (request, 'blog/dashboard.html')
#Login
def user_Login(request):
 if not request.user.is_authenticated:
   if request.method == "POST":
    form = LoginForm(request=request, data=request.POST)
    if  form.is_valid():
      uname =form.cleaned_data['username']
      upass =form.cleaned_data['password']
      user = authenticate(username=uname,password=upass)
      if user is None:
       login(request,user)
       messages.success(request,'Logged In Successfully! ')
       return HttpResponseRedirect('/dashboard/')
   else:
     form=LoginForm()
   return render(request,'blog/signin.html',{'form':form})
 else:
   return HttpResponseRedirect('/dashboard/')
 


#sgnup form
def signup(request):
 if request.method == 'POST':
   fm = SignUpForm(request.POST)
   if fm.is_valid():
    messages.success(request, 'Congratulation! Yoy have become an  Aurthor.')
    fm.save()
    #return HttpResponseRedirect('blog/signin.html')
 else:
  fm = SignUpForm()
 return render (request, 'blog/signup.html',{'form':fm})

def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/')

