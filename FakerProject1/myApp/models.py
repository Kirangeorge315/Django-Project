from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    marks=models.FloatField()
    dob=models.DateField()
    email=models.EmailField()


# Create your models here.
