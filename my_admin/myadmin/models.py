from django.db import models

import time
# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)

    room = models.OneToOneField(ClassRoom)

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom)

    # 同时显示当前时间，这定义过方法后，在admin模块中
    # list_display 处添加这个显示项，函数名
    def curTime(self):
        return time.time()

    def __str__(self):
        return self.name
