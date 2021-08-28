from django.contrib import admin
from Applications.Student.models import Student, JoinedCourse, JoinedTutorial


# Student模型的管理器
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'phone', 'email')

# JoinedCourse模型的管理器
@admin.register(JoinedCourse)
class JoinedCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'course')

# JoinedTutorial模型的管理器
@admin.register(JoinedTutorial)
class JoinedTutorialAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutorial')
