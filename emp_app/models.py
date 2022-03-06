from django.db import models
from . import *

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,default=None)
    location = models.CharField(max_length=50,default=None)
    
    def  __str__(self):
        return self.name  
    
class Role(models.Model):
    name = models.CharField(max_length=50,default=None)
    
    def  __str__(self):
        return self.name  
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department,default=None,on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role,default=None,on_delete=models.CASCADE)
    phone  = models.IntegerField()
    hire_date = models.DateField()   
    
    def  __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)     