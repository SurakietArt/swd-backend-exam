from rest_framework import serializers

from apis.models.classrooms_model import ClassRooms
from apis.models.schools_model import Schools
from apis.models.students_model import Students
from apis.models.teachers_model import Teachers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = "__all__"


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRooms
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
