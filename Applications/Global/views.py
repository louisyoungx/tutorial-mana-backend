import json
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.views import View
from django.conf import settings

from Applications.Student.models import Student
from Applications.Teacher.models import Teacher

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from Applications.Global.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class Token(View):

    def get(self,request):
        token = get_token(request)
        return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")

# 索引页面
class IndexView(View):
    '''索引页面（登陆、注册）'''

    def get(self, request):
        '''索引页面'''
        pass

    def post(self, request):
        uid = request.POST.get('uid')
        user = authenticate(uid=uid)

    def register(self, uid, type):
        # 进行业务处理：注册
        user = User.objects.create_user(uid)
        user.is_active = 0

        if type == 'student':
            student = Student()
            student.user = user
            student.uid = uid
            user.save()
            student.save()

        if type == 'teacher':
            teacher = Teacher()
            teacher.user = user
            teacher.uid = uid
            user.save()
            teacher.save()