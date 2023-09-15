from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed for the Student model

class ClassTiming(models.Model):
    date = models.DateField()
    time = models.TimeField()
    class_name = models.CharField(max_length=100)
    # Add more fields as needed for the ClassTiming model
