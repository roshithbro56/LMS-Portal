
from django.db import models
from django.contrib.auth.models  import User

class StudentProfile(models.Model):
    
    GENDER_CHOICES= (
        
        ('male','Male'),
        ('female','Female'),
        ('other' , 'Other')
    )
    user  =  models.OneToOneField(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    phone_number  =models.CharField(max_length=20)
    email = models.EmailField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)

    def __str__(self):
        return f"Student: {self.user.username}"


class  TeacherProfile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=10,decimal_places=2)
    duration = models.CharField(max_length=100)


    def __str__(self):
        return f"Teacher: {self.user.username}"