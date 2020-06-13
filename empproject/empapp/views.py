from django.shortcuts import render
from empapp.models import Employee
# Create your views here.
def index(request):
    return render(request,'empapp/index.html')

def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'empapp/mazdur.html',context=my_dict)
