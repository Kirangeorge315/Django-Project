from django import forms
class Student(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    marks=forms.FloatField()
    place=forms.CharField()
