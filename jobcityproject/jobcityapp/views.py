from django.shortcuts import render
from jobcityapp.models import *
 # Create your views here.
def Home_Page_view(request):
    return render(request,'jobcityapp/index.html')
def Hyd_Jobs_view(request):
    Hyd_Jobs_list=Hydjobs.objects.all()
    return render(request,'jobcityapp/hydjob.html',{'Hyd_Jobs_list':Hyd_Jobs_list})
def Blore_Jobs_view(request):
    Blr_Jobs_list=Blrjobs.objects.all()
    return render(request,'jobcityapp/banglorejob.html',{'Blr_Jobs_list':Blr_Jobs_list})
def Pune_Jobs_view(request):
    Pune_Jobs_list=punejobs.objects.all()
    return render(request,'jobcityapp/punejob.html',{'Pune_Jobs_list':Pune_Jobs_list})
def Chennai_Jobs_view(request):
    Chennai_Jobs_list=Chennaijobs.objects.all()
    return render(request,'jobcityapp/chennaijob.html',{'Chennai_Jobs_list':Chennai_Jobs_list})
