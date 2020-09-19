from rest_framework import serializers
from MySer.models import *

# 此文件用来存放序列化器

class StudentSerializer(serializers.ModelSerializer):
    '''
    里面写的是每一个需要序列化/反序列化的字段
    跟定义模型中的基本一致
    包括数据长度保持一致最好
    '''
    #name = serializers.CharField(label='姓名',max_length=20)
    #age = serializers.IntegerField()

    from MySer.models import *

    class Meta:
        # 负责告诉它，你对应student数型就可以了，student有什么你就也有什么
        model = Student
        #fields = ['name','age']
        # 这句话告诉序列器你直接把模型student中所有的数型都给我序列化
        # 不需要上面的那个一一列出
        fields = ['__all__']


