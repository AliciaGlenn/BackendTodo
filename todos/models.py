from django.db import models

# Create your models here.
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)