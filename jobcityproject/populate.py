import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobcityproject.settings')
django.setup()
from jobcityapp.models import *
from faker import Faker
from random import *
faker=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('Project Manager','Team Lead','Software Enginner','DBA'))
        felligibility=faker.random_element(elements=('MCA','B.Tech'))
        feaddress=faker.address()
        femail=faker.email()
        fphoneno=phonenumbergen()
        hyd_record=Hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phoneno=fphoneno)
        Blore_recordt=Blrjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phoneno=fphoneno)
        Pune_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phoneno=fphoneno)
        Chennai_record=Chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phoneno=fphoneno)
populate(30)
populate(30)
