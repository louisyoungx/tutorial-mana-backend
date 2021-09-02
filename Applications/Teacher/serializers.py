from Applications.Teacher.models import Teacher, Course, Tutorial
from rest_framework import serializers

class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = ['uid', 'name', 'phone', 'email']

class CourseSerializer(serializers.Serializer):
    teacher_id = serializers.SlugRelatedField(slug_field="uid", source="teacher", queryset=Teacher.objects.all(), label='老师')
    name = serializers.CharField(max_length=6, label='课程')
    term = serializers.CharField(max_length=10, label='学期')
    nums = serializers.IntegerField(default=0, label='参加人数')
    limit = serializers.IntegerField(default=0, label='人数限制')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Snippet 实例。
        """
        teacher = Teacher.objects.get(uid='123456')
        print(teacher)
        course = Course(teacher=teacher, name=validated_data['name'], term=validated_data['term'], nums=validated_data['nums'], limit=validated_data['limit'])
        course.save()
        return course

class TutorialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tutorial
        fields = ['course', 'teacher', 'start_time', 'end_time', 'place', 'joined_num']
