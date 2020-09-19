from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from case01.serializers import *
from case01.models import Student

class StudentVS(viewsets.ModelViemset):
    serializer_class = StudentSer
    queryset = Student.object.all()

