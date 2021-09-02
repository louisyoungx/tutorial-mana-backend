from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework import permissions
from Applications.Teacher.models import Teacher, Course, Tutorial
from Applications.Teacher.serializers import TeacherSerializer, CourseSerializer, TutorialSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class TeacherViewSet(viewsets.ModelViewSet):
    """
    对教师列表的API操作
    """
    queryset = Teacher.objects.all().order_by('-creat_time')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('uid',)
    search_fields = ('email',)

    @action(methods=['post'], detail=True)
    def login(self, request, uid=None):
        teacher = Teacher.objects.filter(uid=uid)
        serializer = self.get_serializer(teacher, many=True)
        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    """
    对课程列表的API操作
    """
    queryset = Course.objects.all().order_by('-creat_time')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
    search_fields = ('name', 'teacher',)

class TutorialViewSet(viewsets.ModelViewSet):
    """
    对辅导列表的API操作
    """
    queryset = Tutorial.objects.all().order_by('-creat_time')
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]