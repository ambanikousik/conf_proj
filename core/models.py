from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# ENUMS


class User(AbstractUser): 
    fist_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    photo=models.ImageField(blank=True,null=True)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.email



class Task(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=450)
    due_date=models.DateField()

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    def __set__(self):
        return self.title

 




# class Faculty(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     designation = models.ForeignKey(Designation,on_delete=models.DO_NOTHING,blank=True,null=True)
#     iub_id = models.CharField(max_length=15)
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#     room_number = models.CharField(max_length=50,blank=True,null=True)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     secondary_phone = models.CharField(max_length=20,blank=True,null=True)
#     portfolio = models.CharField(max_length=500,blank=True,null=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.first_name+self.last_name

# class Student(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
    
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#     iub_id = models.CharField(max_length=8)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     address = models.CharField(max_length=250,blank=True,null=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.first_name+self.last_name