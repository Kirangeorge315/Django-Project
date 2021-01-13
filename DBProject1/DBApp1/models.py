from django.db import models

class Student(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=30)
    marks=models.FloatField()
    def __str__(self):
        return str(self.number)
