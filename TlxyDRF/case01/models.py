from django.db import models


# Create your models here.

class ClassRoom(models.Model):
    roomName = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)

class Teacher(models.Model):
    course = models.CharField(max_length=5)
    name = models.CharField(max_length=5)
    age = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField()

