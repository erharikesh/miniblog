from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
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
def signin(request):
    return render (request, 'blog/signin.html')
    #sgnup form
def signup(request):
 fm = SignUpForm()
 return render (request, 'blog/signup.html',{'form':fm})

def user_logout(request):
  return HttpResponseRedirect('/')

