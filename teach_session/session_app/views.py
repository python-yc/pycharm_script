from django.shortcuts import render

# Create your views here.



# from django.core.paginator import Paginator
# def mySession(request):
#     print(type(request.session))
#     print(request.session)
#     # 如果session中没有teacher_name的值，则返回NoName
#     print(request.session.get("teacher_name","NoName"))
#
#     # 清除session所有的值
#     request.session.clear()
#
#     print("In mySession")
#     return None
# from django.views.generic import ListView
#
# class StudentListView(ListView):
#     '''
#     需要设置两个主要内容
#     1.queryset：数据集合
#     2.template_name：模板名称
#     '''
#     queryset = Student.objects.all().filter(gender="man")
#
#     template_name = "student_list.html"
#
#
# from teach_session.session_app.models import *
# def student(request):
#     '''
#     请求所有学生的详情列表
#     :param request:
#     :return:
#     '''
#     # 大约有10000名学生，可以用分页实现，比如一页50
#     stus = Student.objects.all()
#     # 两个参数
#     # 1.数据来源，也即是从数据库中查询出的数据
#     # 2.单页返回数据量
#     p = Paginator(stus,50)
#     # 对Paginator进行设置或者对变量属相使用
#     print(p.count)  # p里面有多少数据
#     print(p.num_pages)# 页面总数
#     print(p.page_range)# 页码列表，从1开始
#
#     # 取得第三页的内容
#     # 如果页码不存在，报异常invalidPage
#     p.page(3)
#     return stus





