from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from MySer.models import Student
from MySer.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response


class StudentVS(viewsets.ModelViewSet):
    serializer_class = StudentSer
    queryset = Student.objects.all()


class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self):
        '''
        处理业务
        与数据库交互
        :return: 
        '''
        print("In APIView get")
        #return None
        stus = Student.objects.all()
        ser = StudentSerializer(stus,many=True)
        return Response(data=ser.data)





