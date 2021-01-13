from django.db import models
from django.urls import reverse
class Student(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    marks=models.FloatField()
    place=models.CharField(max_length=40)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})




