from django.db import models

class student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
    
