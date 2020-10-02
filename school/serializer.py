from rest_framework import serializers
from .models import School, Course, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # 获取教师的id和name，用于前端展示
    teachers = serializers.SerializerMethodField()

    def get_teachers(self, obj):
        return obj.teacher_set.values()

    class Meta:
        model = Course
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    def get_courses(self, obj):
        return obj.course_set.values()
    class Meta:
        model = Teacher
        fields = "__all__"

