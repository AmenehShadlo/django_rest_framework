from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import  Student,Book
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__" #["Name","Family"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

