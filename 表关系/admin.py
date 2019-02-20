# 向admin中注册模型（model）
from django.contrib import admin

# Register your models here.
from .models import Department,Student,StudentDetail,Course
# 创建模型类对应的管理页面admin的类
class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_id','c_name']
    list_display_links = ['c_id','c_name']
    list_per_page = 2



admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentDetail)
# 将自定义的类放到register方法中注册使用
admin.site.register(Course,CourseAdmin)