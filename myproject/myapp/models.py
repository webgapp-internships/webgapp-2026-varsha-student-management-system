from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    

