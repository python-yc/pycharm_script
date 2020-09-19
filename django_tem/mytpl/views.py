from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def one(request):
    # 这个request必须有
    return render(request,r'one.html')

def two(request):

    # 使用存放向模板传递的数据
    ct = dict()
    ct["name"] = "xiaoming"
    ct["age"] = 18
    # 这个request必须有
    return render(request,r'two.html',context=ct)

def three(request):
    ct = dict()
    ct["score"] = [99,98,97,83,87]
    return render(request,r'three.html',context=ct)

def four(request):
    ct = dict()
    ct["name"] = "xiaosi"
    return render(request,r'four.html',context=ct)

def five_get(request):
    return render(request,r"five_get.html")

def five_post(request):
    print(request.POST)
    return render(request,r"one.html")
