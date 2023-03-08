from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    fee=models.IntegerField(default=0)

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    stud_name=models.CharField(max_length=255)
    stud_address=models.CharField(max_length=255)
    stud_age=models.IntegerField(null=True,blank=True,default=None)
    join_date=models.DateField()   


class Teacher(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    number=models.CharField(max_length=255)    
    image=models.ImageField(default="default1.jpg",blank=True,upload_to="image/", null=True) 

    