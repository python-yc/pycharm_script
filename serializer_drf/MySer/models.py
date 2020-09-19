from django.db import models

# Create your models here.

# 在使用时，命令行添加过数据记得使用save保存
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    score = models.IntegerField()

