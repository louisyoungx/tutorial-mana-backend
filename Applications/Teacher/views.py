from rest_framework import viewsets
from rest_framework import permissions
from Applications.Teacher.models import Teacher, Course, Tutorial
from Applications.Teacher.serializers import TeacherSerializer, CourseSerializer, TutorialSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    对学生列表的API操作
    """
    queryset = Teacher.objects.all().order_by('-creat_time')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """
    对学生列表的API操作
    """
    queryset = Course.objects.all().order_by('-creat_time')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class TutorialViewSet(viewsets.ModelViewSet):
    """
    对学生列表的API操作
    """
    queryset = Tutorial.objects.all().order_by('-creat_time')
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]
