from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'advtemp/home.html')

def movies_view(request):
    return render(request,'advtemp/movies.html')

def politics_view(request):
    return render(request,'advtemp/politics.html')

def sports_view(request):
    return render(request,'advtemp/sports.html')
