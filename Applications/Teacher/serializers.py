from Applications.Teacher.models import Teacher, Course, Tutorial
from rest_framework import serializers



class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'uid', 'name', 'avatar', 'wechat_id', 'phone', 'email', 'location']



class CourseSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, max_length=6, label='ID')
    teacher_id = serializers.SlugRelatedField(slug_field="id", source="teacher", queryset=Teacher.objects.all(),
                                              label='老师id')
    teacher_name = serializers.SlugRelatedField(required=False, slug_field="name", source="teacher", queryset=Teacher.objects.all(),
                                              label='老师姓名')
    teacher_phone = serializers.SlugRelatedField(required=False, slug_field="phone", source="teacher", queryset=Teacher.objects.all(),
                                              label='老师手机')
    teacher_avatar = serializers.SlugRelatedField(required=False, slug_field="avatar", source="teacher", queryset=Teacher.objects.all(),
                                              label='老师头像')
    name = serializers.CharField(max_length=10, label='课程')
    wallpaper = serializers.URLField(max_length=200, min_length=None, allow_blank=True, label='壁纸')
    describe = serializers.CharField(max_length=50, label='描述')
    term = serializers.CharField(max_length=10, label='学期')
    nums = serializers.IntegerField(required=False, default=0, label='参加人数')
    limit = serializers.IntegerField(required=False, default=0, label='人数限制')
    creat_time = serializers.CharField(required=False, label='创建时间')
    is_delete = serializers.BooleanField(required=False, default=False, label='是否删除')

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
    id = serializers.CharField(required=False, max_length=6, label='ID')
    course_id = serializers.SlugRelatedField(slug_field="id", source="course", queryset=Course.objects.all(),
                                             label='所属课程')
    course_name = serializers.SlugRelatedField(required=False, slug_field="name", source="course", queryset=Course.objects.all(),
                                             label='课程名')
    teacher_id = serializers.SlugRelatedField(required=False, slug_field="id", source="teacher", queryset=Teacher.objects.all(),
                                             label='所属老师')
    teacher_name = serializers.SlugRelatedField(required=False, slug_field="name", source="teacher", queryset=Teacher.objects.all(),
                                             label='老师姓名')
    teacher_phone = serializers.SlugRelatedField(required=False, slug_field="phone", source="teacher", queryset=Teacher.objects.all(),
                                             label='老师手机')
    teacher_email = serializers.SlugRelatedField(required=False, slug_field="email", source="teacher", queryset=Teacher.objects.all(),
                                             label='老师邮箱')
    teacher_avatar = serializers.SlugRelatedField(required=False, slug_field="avatar", source="teacher", queryset=Teacher.objects.all(),
                                             label='老师头像')
    describe = serializers.CharField(max_length=50, label='描述')
    start_time = serializers.DateTimeField(label='开始时间')
    duration_time = serializers.FloatField(label='持续时间')
    place = serializers.CharField(max_length=50, label='地点')
    wallpaper = serializers.SlugRelatedField(required=False, slug_field="wallpaper", source="course", queryset=Course.objects.all(),
                                              label='壁纸')
    joined_num = serializers.IntegerField(required=False, default=0, label='已加入人数')
    is_done = serializers.BooleanField(required=False, default=False, label='是否完成')
    creat_time = serializers.CharField(required=False, label='创建时间')
    is_delete = serializers.BooleanField(required=False, default=False, label='是否删除')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Snippet 实例。
        """
        for item in validated_data:
            print(item, validated_data[item])
        course = Course.objects.get(id=str(validated_data['course']))
        teacher = course.teacher

        tutorial = Tutorial()
        tutorial.course = course
        tutorial.teacher = teacher
        tutorial.describe = validated_data['describe']
        tutorial.start_time = validated_data['start_time']
        tutorial.duration_time = validated_data['duration_time']
        tutorial.place = validated_data['place']
        tutorial.joined_num = 0
        tutorial.save()
        return tutorial
