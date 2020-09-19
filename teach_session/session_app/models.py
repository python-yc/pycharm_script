from django.db import models

import time
# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)

    room = models.OneToOneField(ClassRoom,default="")

    def curTime(self):
        return time.time()

    curTime.short_description = "当前时间"
    # 时间函数实现排序，需要依赖其它数据
    curTime.admin_order_field = "name"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom,default="")

    def __str__(self):
        return self.name

