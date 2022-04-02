from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Family=models.CharField(max_length=100)
    Code=models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()  

class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()

class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.PROTECT)
    Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()