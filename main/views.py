from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def user_login(request):
    return render(request,'main/home.html')