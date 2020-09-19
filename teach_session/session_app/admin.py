from django.contrib import admin


from session_app.models import Student, ClassRoom, Teacher
# Register your models here.

# 这下面的启用即可修改完成，根据自己定义名字
# admin.site.site_header = "欢迎来到django课题"
# admin.site.site_title = "南京欢迎你"
# admin.site.index_title = "阿财要打一片天下"


class ClassRoomAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_top = False
    actions_on_bottom = True
    list_display = ["name","room","curTime"] # 若想显示字相关段，把这个注释去掉即可

    fieldsets = (
        ("基本信息", {"fields":["name",]}),
        ("其它信息",{"fields": ["room","course"]}),
    )

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student,StudentAdmin)
admin.site.register(ClassRoom,ClassRoomAdmin)
admin.site.register(Teacher,TeacherAdmin)

# 不添加装饰器可直接使用以下写法即可
# admin.site.register(Student)
# admin.site.register(ClassRoom)
# admin.site.register(Teacher)
