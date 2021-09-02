from rest_framework import viewsets
from rest_framework import permissions
from Applications.Student.models import Student, JoinedCourse, JoinedTutorial
from Applications.Student.serializers import StudentSerializer, JoinedCourseSerializer, JoinedTutorialSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    对学生列表的API操作
    """
    queryset = Student.objects.all().order_by('-creat_time')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class JoinedCourseViewSet(viewsets.ModelViewSet):
    """
    对学生课程的API操作
    """
    queryset = JoinedCourse.objects.all().order_by('-creat_time')
    serializer_class = JoinedCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class JoinedTutorialViewSet(viewsets.ModelViewSet):
    """
    对学生辅导的API操作
    """
    queryset = JoinedTutorial.objects.all().order_by('-creat_time')
    serializer_class = JoinedTutorialSerializer
    permission_classes = [permissions.IsAuthenticated]
