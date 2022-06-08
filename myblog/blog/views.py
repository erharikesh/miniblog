from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
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
def user_Login(request):
  form =LoginForm
  return render (request, 'blog/signin.html',{'form':form})
#sgnup form
def signup(request):
 if request.method == 'POST':
   fm = SignUpForm(request.POST)
   if fm.is_valid():
    messages.success(request, 'Congratulation! Yoy have become an  Aurthor.')
    fm.save()
 else:
  fm = SignUpForm()
 return render (request, 'blog/signup.html',{'form':fm})

def user_logout(request):
  return HttpResponseRedirect('/')

