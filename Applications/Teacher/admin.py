from django.contrib import admin
from Applications.Teacher.models import Teacher, Course, Tutorial


# Teacher模型的管理器
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'avatar', 'wechat_id', 'phone', 'email')

# Course模型的管理器
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'name', 'term', 'nums', 'limit')

# Tutorial模型的管理器
@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('course', 'teacher', 'start_time', 'duration_time', 'place', 'joined_num')
