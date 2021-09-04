from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from Applications.Teacher.models import Teacher, Course, Tutorial
from db.base_model import BaseModel


# Create your models here.

# 用户模型类
class Student(BaseModel):
    '''学生模型类'''
    uid = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name='学号')
    name = models.CharField(max_length=6, blank=True, verbose_name='姓名')
    avatar = models.URLField(default='http://www.louisyoung.site:8002/TutorialManage/avatar.jpg', blank=True, verbose_name='头像')
    wechat_id = models.CharField(max_length=30, blank=True, null=True, verbose_name='微信openid')
    phone = models.CharField(max_length=11, blank=True, verbose_name='手机号')
    email = models.CharField(max_length=20, blank=True, verbose_name='邮箱')

    def __str__(self):
        return self.uid

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

class JoinedCourse(BaseModel):
    """学生参加的课程"""
    student = models.ForeignKey(Student, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属学生')
    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属老师')
    course = models.ForeignKey(Course, blank=False, null=False, on_delete=models.CASCADE, verbose_name='参加的课程')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "joined_course"
        verbose_name = "学生已参加的课程"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

class JoinedTutorial(BaseModel):
    """学生参加的辅导"""
    student = models.ForeignKey(Student, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属学生')
    tutorial = models.ForeignKey(Tutorial, blank=False, null=False, on_delete=models.CASCADE, verbose_name='辅导')
    is_done = models.BooleanField(default=False, verbose_name='是否完成')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "joined_tutorial"
        verbose_name = "学生已参加的辅导"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
