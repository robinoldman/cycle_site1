from django.shortcuts import render
from cycle.forms import LoginForm

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def user_login(request):
    return render(request,'registration/login.html')