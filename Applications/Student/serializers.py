from Applications.Student.models import Student, JoinedCourse, JoinedTutorial
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ['uid', 'name', 'phone', 'email']

class JoinedCourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JoinedCourse
        fields = ['student', 'teacher', 'course']

class JoinedTutorialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JoinedTutorial
        fields = ['student', 'tutorial']
