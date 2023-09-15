from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_superadmin = models.BooleanField(default=False)  # Indicates if the admin is a superadmin with more authority
    # Add more fields as needed for the Admin model

class ClassTiming(models.Model):
    date = models.DateField()
    time = models.TimeField()
    class_name = models.CharField(max_length=100)
    # Add more fields as needed for the ClassTiming model
