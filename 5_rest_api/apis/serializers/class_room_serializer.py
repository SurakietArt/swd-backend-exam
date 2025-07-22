from typing import List, Any, Dict

from rest_framework import serializers

from apis.models.classrooms import ClassRooms
from apis.models.students import Students
from apis.models.teachers import Teachers
from apis.serializers.student_serializer import StudentsSerializer
from apis.serializers.teacher_serializer import TeacherSerializer


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRooms
        fields = "__all__"


class ClassRoomDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField("_list_teachers")
    students = serializers.SerializerMethodField("_list_students")

    class Meta:
        model = ClassRooms
        fields = "__all__"

    @staticmethod
    def _list_teachers(obj: ClassRooms) -> List[Dict[str, Any]]:
        teachers = Teachers.objects.filter(class_room=obj)
        return TeacherSerializer(teachers, many=True).data

    @staticmethod
    def _list_students(obj: ClassRooms) -> List[Dict[str, Any]]:
        students = Students.objects.filter(class_room=obj)
        return StudentsSerializer(students, many=True).data
