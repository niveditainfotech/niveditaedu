
from django.db import models

# Create your models here.

class Forms(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    place=models.CharField(max_length=50)
    course=models.CharField(max_length=50)

    def __str__(self):
        return self.name