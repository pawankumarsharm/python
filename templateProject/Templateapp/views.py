from django.shortcuts import render
import datetime
# Create your views here.
def dateinfo(request):
    date=datetime.datetime.now()
    name='pawan'
    my_dict={'msg':date,'guest':name}
    return render(request,'Templateapp/print.html',context=my_dict)
