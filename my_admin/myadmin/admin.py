from django.contrib import admin

# Register your models here.

from myadmin.models import Student,ClassRoom,Teacher

class ClassRoomAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    # 每页显示数量
    list_per_page = 2
    # 操作选项框在下
    actions_on_top = False
    # 或者这样
    # actions_on_bottom = True
    # 控制内容是否显示
    list_display = ["name","room","curTime"]
    serach_fields = ["name"]

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student.StudentAdmin)
admin.site.register(ClassRoom.ClassRoomAdmin)
admin.site.register(Teacher.TeacherAdmin)


# admin.site.register(Student)
# admin.site.register(ClassRoom)
# admin.site.register(Teacher)
