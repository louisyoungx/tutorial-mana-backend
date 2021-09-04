from Applications.Teacher.models import Teacher, Course, Tutorial
from rest_framework import serializers



class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['uid', 'name', 'avatar', 'wechat_id', 'phone', 'email']



class CourseSerializer(serializers.Serializer):
    teacher_id = serializers.SlugRelatedField(slug_field="uid", source="teacher", queryset=Teacher.objects.all(),
                                              label='所属老师')
    name = serializers.CharField(max_length=6, label='课程')
    wallpaper = serializers.URLField(max_length=200, min_length=None, allow_blank=True)
    describe = serializers.CharField(max_length=50, label='描述')
    term = serializers.CharField(max_length=10, label='学期')
    nums = serializers.IntegerField(default=0, label='参加人数')
    limit = serializers.IntegerField(default=0, label='人数限制')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Course 实例。
        """
        teacher = Teacher.objects.get(uid=validated_data['teacher'])

        course = Course()
        course.teacher = teacher
        course.name = validated_data['name']
        course.wallpaper = validated_data['wallpaper']
        course.describe = validated_data['describe']
        course.term = validated_data['term']
        course.nums = validated_data['nums']
        course.limit = validated_data['limit']
        course.save()

        return course



class TutorialSerializer(serializers.Serializer):
    course_id = serializers.SlugRelatedField(slug_field="id", source="course", queryset=Course.objects.all(),
                                             label='所属课程')
    describe = serializers.CharField(max_length=50, label='描述')
    start_time = serializers.DateTimeField(label='开始时间')
    end_time = serializers.DateTimeField(label='结束时间')
    place = serializers.CharField(max_length=50, label='地点')
    joined_num = serializers.IntegerField(default=0, label='已加入人数')
    is_done = serializers.BooleanField(default=False, label='是否完成')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Snippet 实例。
        """
        course = Course.objects.get(id=str(validated_data['course']))
        teacher = course.teacher

        tutorial = Tutorial()
        tutorial.course = course
        tutorial.teacher = teacher
        tutorial.describe = validated_data['describe']
        tutorial.start_time = validated_data['start_time']
        tutorial.end_time = validated_data['end_time']
        tutorial.place = validated_data['place']
        tutorial.joined_num = 0
        tutorial.save()
        return tutorial
