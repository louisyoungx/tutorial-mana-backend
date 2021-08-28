from Applications.Teacher.models import Teacher, Course, Tutorial
from rest_framework import serializers


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = ['uid', 'name', 'phone', 'email']

class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['teacher', 'name', 'term', 'nums', 'limit']

class TutorialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tutorial
        fields = ['course', 'teacher', 'start_time', 'end_time', 'place', 'joined_num']
