from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from db.base_model import BaseModel

# Create your models here.

# 用户模型类
class Student(BaseModel):
    '''学生模型类'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE, verbose_name='学生')
    id = models.CharField(max_length=10, blank=False, null=False, verbose_name='学号')
    name = models.CharField(max_length=6, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    email = models.CharField(max_length=20, blank=True, verbose_name='邮箱')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class AppendCourse(BaseModel):
    """学生参加的课程"""
    student = models.ForeignKey(Student, blank=False, null=False, verbose_name='所属学生')
    teacher = models.ForeignKey(Teacher, blank=False, null=False, verbose_name='所属老师')
    course = models.ForeignKey(Course, blank=False, null=False, verbose_name='参加的课程')

    def __str__(self):
        return self.course


    class Meta:
        db_table = "append_course"
        verbose_name = "学生参加的课程"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class JoinedTutorial(BaseModel):
    """学生参加的课程"""
    student = models.ForeignKey(Student, blank=False, null=False, verbose_name='所属学生')
    tutorial = models.ForeignKey(Tutorial, blank=False, null=False, verbose_name='所属老师')

    def __str__(self):
        return self.course


    class Meta:
        db_table = "JoinedTutorial"
        verbose_name = "已参加的辅导"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

