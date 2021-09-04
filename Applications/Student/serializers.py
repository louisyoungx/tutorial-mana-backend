from rest_framework import serializers
from Applications.Teacher.models import Teacher, Course, Tutorial
from Applications.Student.models import Student, JoinedCourse, JoinedTutorial

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['uid', 'name', 'phone', 'email']


class JoinedCourseSerializer(serializers.Serializer):
    student_id = serializers.SlugRelatedField(slug_field="uid", source="student", queryset=Student.objects.all(),
                                              label='所属学生')
    teacher_id = serializers.SlugRelatedField(slug_field="uid", source="teacher", queryset=Teacher.objects.all(),
                                              label='所属老师')
    course_id = serializers.SlugRelatedField(slug_field="id", source="course", queryset=Course.objects.all(),
                                             label='所属课程')
    is_delete = serializers.BooleanField(default=False, label='是否结束')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 JoinedCourse 实例。
        """
        student = Student.objects.get(uid=validated_data['student'])
        course = Course.objects.get(id=str(validated_data['course']))
        teacher = course.teacher

        joined_course = JoinedCourse()
        joined_course.student = student
        joined_course.course = course
        joined_course.teacher = teacher
        joined_course.save()

        return joined_course


class JoinedTutorialSerializer(serializers.Serializer):
    student_id = serializers.SlugRelatedField(slug_field="uid", source="student", queryset=Student.objects.all(),
                                              label='所属学生')
    tutorial_id = serializers.SlugRelatedField(slug_field="id", source="tutorial", queryset=Tutorial.objects.all(),
                                               label='所属辅导')
    is_delete = serializers.BooleanField(default=False, label='是否结束')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 JoinedCourse 实例。
        """
        student = Student.objects.get(uid=validated_data['student'])
        tutorial = Tutorial.objects.get(id=str(validated_data['tutorial']))

        joined_tutorial = JoinedTutorial()
        joined_tutorial.student = student
        joined_tutorial.tutorial = tutorial
        joined_tutorial.save()

        return joined_tutorial
