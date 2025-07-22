from rest_framework import serializers

from apis.models.teachers import Teachers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"
