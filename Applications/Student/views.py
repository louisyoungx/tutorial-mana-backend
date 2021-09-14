from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from Applications.Student.models import Student, JoinedCourse, JoinedTutorial
from Applications.Student.serializers import StudentSerializer, JoinedCourseSerializer, JoinedTutorialSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    对学生列表的API操作
    """
    queryset = Student.objects.all().order_by('-creat_time')
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('uid', 'name', 'email',)
    search_fields = ('uid', 'name', 'email',)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        #过滤出nid等于多少的对象。
        student = Student.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = StudentSerializer(data=request.data,instance=student,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

class JoinedCourseViewSet(viewsets.ModelViewSet):
    """
    对学生课程的API操作
    """
    queryset = JoinedCourse.objects.all().order_by('-creat_time')
    serializer_class = JoinedCourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('student_id', 'teacher_id', 'course_id', 'is_delete',)
    search_fields = ('student_id', 'teacher_id', 'course_id', 'is_delete',)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        #过滤出nid等于多少的对象。
        joined_course = JoinedCourse.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = JoinedCourseSerializer(data=request.data,instance=joined_course,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        #执行ORM删除数据的操作
        # joined_course = JoinedCourse.objects.get(id=str(pk)).delete()
        joined_course = JoinedCourse.objects.get(id=str(pk))
        joined_course.is_delete = True
        joined_course.save()
        return Response('success', status=200)

class JoinedTutorialViewSet(viewsets.ModelViewSet):
    """
    对学生辅导的API操作
    """
    queryset = JoinedTutorial.objects.all().order_by('-creat_time')
    serializer_class = JoinedTutorialSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('student_id', 'tutorial_id', 'is_delete',)
    search_fields = ('student_id', 'tutorial_id', 'is_delete',)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        # 过滤出nid等于多少的对象。
        joined_tutorial = JoinedTutorial.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = JoinedTutorialSerializer(data=request.data, instance=joined_tutorial, many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        # 执行ORM删除数据的操作
        # joined_tutorial = Course.objects.get(id=str(pk)).delete()
        joined_tutorial = JoinedTutorial.objects.get(id=str(pk))
        joined_tutorial.is_delete = True
        joined_tutorial.save()
        return Response('success', status=200)