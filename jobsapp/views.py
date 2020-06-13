from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinf(request):
    s='<h1>Hydrabad job information<h1>'
    return HttpResponse(s)

def punejobsinf(request):
    s1='<h1>pune job information<h1>'
    return HttpResponse(s1)

def chennaijobsinf(request):
    s2='<h1>chennai job information<h1>'
    return HttpResponse(s2)
