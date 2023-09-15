from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed for the Admin model
