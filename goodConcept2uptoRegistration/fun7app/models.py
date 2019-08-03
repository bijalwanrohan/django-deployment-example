from django.db import models

from django.contrib.auth.models import User


class Student(models.Model):

    allfields= models.OneToOneField(User,on_delete=models.CASCADE)
    NameStudent=models.CharField(max_length=200)
    Email_blnk=models.EmailField(blank=True)
    aadhaar=models.IntegerField(unique=True)  # by default all will be blank=False
    profile_pic_blnk=models.ImageField(blank=True,upload_to='funapp/profilePics')

class Father(models.Model):
    FatherOfStudent=models.ForeignKey(Student,on_delete=models.CASCADE)
    FatherName=models.CharField(max_length=200)
