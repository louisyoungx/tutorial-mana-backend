from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from db.base_model import BaseModel

# Create your models here.

# 用户模型类
class Teacher(BaseModel):
    '''教师模型类'''
    uid = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name='工号')
    name = models.CharField(max_length=6, blank=True, verbose_name='姓名')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号')
    email = models.EmailField(max_length=20, blank=True, verbose_name='邮箱')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Course(BaseModel):
    """教师管理的课程"""
    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属老师')
    name = models.CharField(max_length=6, verbose_name='课程')
    term = models.CharField(max_length=10, verbose_name='学期')
    nums = models.IntegerField(default=0, verbose_name='参加人数')
    limit = models.IntegerField(default=0, blank=False, verbose_name='人数限制')

    def __str__(self):
        return self.name


    class Meta:
        db_table = "course"
        verbose_name = "教师管理的课程"
        verbose_name_plural = verbose_name
        get_latest_by = 'teacher'


class Tutorial(BaseModel):
    """已发布的辅导"""
    course = models.ForeignKey(Course, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属课程')
    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属老师')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    place = models.CharField(max_length=50, verbose_name='地点')
    joined_num = models.IntegerField(default=0, verbose_name='已加入人数')


    def __str__(self):
        return self.course


    class Meta:
        db_table = "tutorial"
        verbose_name = "已发布的辅导"
        verbose_name_plural = verbose_name
        get_latest_by = 'teacher'



