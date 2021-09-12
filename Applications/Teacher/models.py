from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from db.base_model import BaseModel



# 用户模型类
class Teacher(BaseModel):
    '''教师模型类'''
    uid = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name='工号')
    name = models.CharField(max_length=6, blank=True, verbose_name='姓名')
    avatar = models.URLField(default='http://www.louisyoung.site:8002/TutorialManage/avatar.jpg', blank=True, null=True, verbose_name='头像')
    wechat_id = models.CharField(max_length=30, blank=True, null=True, verbose_name='微信openid')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号')
    email = models.EmailField(max_length=20, blank=True, verbose_name='邮箱')
    location = models.CharField(max_length=20, blank=True, null=True, verbose_name='默认地点')

    def __str__(self):
        return self.uid

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'



class Course(BaseModel):
    """教师管理的课程"""
    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属老师')
    name = models.CharField(max_length=10, verbose_name='课程')
    wallpaper = models.URLField(default='http://www.louisyoung.site:8002/TutorialManage/wallpaper.jpg', blank=True, verbose_name='背景')
    describe = models.CharField(max_length=50, blank=True, null=True, verbose_name='描述')
    term = models.CharField(max_length=10, verbose_name='学期')
    nums = models.IntegerField(default=0, verbose_name='参加人数')
    limit = models.IntegerField(default=0, blank=False, verbose_name='人数限制')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "course"
        verbose_name = "教师管理的课程"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'



class Tutorial(BaseModel):
    """已发布的辅导"""
    course = models.ForeignKey(Course, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属课程')
    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.CASCADE, verbose_name='所属老师')
    describe = models.CharField(max_length=50, blank=True, null=True, verbose_name='描述')
    start_time = models.DateTimeField(verbose_name='开始时间')
    duration_time = models.FloatField(default=2.0, verbose_name='持续时间')
    place = models.CharField(max_length=50, verbose_name='地点')
    joined_num = models.IntegerField(default=0, verbose_name='已加入人数')
    is_done = models.BooleanField(default=False, verbose_name='是否完成')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "tutorial"
        verbose_name = "已发布的辅导"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'



