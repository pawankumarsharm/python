from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'picapp/home.html')

def profile(request):
    return render(request,'picapp/profile.html')
