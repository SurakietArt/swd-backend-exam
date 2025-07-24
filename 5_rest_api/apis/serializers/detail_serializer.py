from rest_framework import serializers

from apis.models.classrooms_model import ClassRooms
from apis.models.schools_model import Schools
from apis.models.students_model import Students
from apis.models.teachers_model import Teachers
from apis.serializers.base_serializer import TeacherSerializer, StudentSerializer, ClassRoomSerializer


class SchoolDetailSerializer(serializers.ModelSerializer):
    count_class_room = serializers.IntegerField(read_only=True)
    count_teacher = serializers.IntegerField(read_only=True)
    count_student = serializers.IntegerField(read_only=True)

    class Meta:
        model = Schools
        fields = "__all__"


class ClassRoomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = ClassRooms
        fields = "__all__"


class TeacherDetailSerializer(serializers.ModelSerializer):
    class_room = ClassRoomSerializer(many=True)

    class Meta:
        model = Teachers
        fields = "__all__"


class StudentDetailSerializer(serializers.ModelSerializer):
    class_room = ClassRoomSerializer()

    class Meta:
        model = Students
        fields = "__all__"

