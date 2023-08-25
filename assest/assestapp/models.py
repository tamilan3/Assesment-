from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class UserTable(AbstractUser):

    groups = models.ManyToManyField(Group,verbose_name = ('groups'),blank=True,related_name='custom_user_set'  )
    user_permissions = models.ManyToManyField(Permission,verbose_name = ('user permissions'),blank=True,related_name='custom_user_set' )
    
    def __str__(self):
        return self.username

class Employee(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=20)
    empDateofJoin = models.DateField()
    salary = models.IntegerField()

    def __str__(self) :
        return self.empName

class Attandancetable(models.Model):
    empId = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Date = models.DateField()
    Attendance = models.BooleanField()
    WorkingHour = models.CharField(max_length=5)
