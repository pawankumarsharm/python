from django.contrib import admin
from empapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
