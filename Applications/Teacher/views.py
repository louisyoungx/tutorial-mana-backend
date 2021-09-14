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
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('uid', 'name', 'phone', 'email',)
    search_fields = ('uid', 'name', 'phone', 'email',)

    # @action(methods=['post'], detail=True)
    # def login(self, request, uid=None):
    #     teacher = Teacher.objects.filter(uid=uid)
    #     serializer = self.get_serializer(teacher, many=True)
    #     return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        #过滤出nid等于多少的对象。
        teacher = Teacher.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = TeacherSerializer(data=request.data,instance=teacher,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)



class CourseViewSet(viewsets.ModelViewSet):
    """
    对课程列表的API操作
    """
    queryset = Course.objects.all().order_by('-creat_time')
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('teacher_id', 'name', 'term', 'is_delete',)
    search_fields = ('teacher_id', 'name', 'term', 'is_delete',)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        #过滤出nid等于多少的对象。
        course = Course.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = CourseSerializer(data=request.data,instance=course,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        #执行ORM删除数据的操作
        # course = Course.objects.get(id=str(pk)).delete()
        course = Course.objects.get(id=str(pk))
        course.is_delete = True
        course.save()
        return Response('success', status=200)



class TutorialViewSet(viewsets.ModelViewSet):
    """
    对辅导列表的API操作
    """
    queryset = Tutorial.objects.all().order_by('-creat_time')
    serializer_class = TutorialSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('teacher_id', 'course_id', 'is_delete',)
    search_fields = ('teacher_id', 'course_id', 'is_delete',)

    @action(methods=['put'], detail=True)
    def put(self, request, pk):
        #过滤出nid等于多少的对象。
        tutorial = Tutorial.objects.get(id=str(pk))
        '''请注意，在序列化时，我们除了传入data参数外，还需告诉序列化组件，我们需要更新哪条数据，也就是instance，
        我们使用的序列化类是三版本的序列化类'''
        serialized_data = CourseSerializer(data=request.data,instance=tutorial,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors)

    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        #执行ORM删除数据的操作
        # tutorial = Tutorial.objects.get(id=str(pk)).delete()
        tutorial = Tutorial.objects.get(id=str(pk))
        tutorial.is_delete = True
        tutorial.save()
        return Response('success', status=200)