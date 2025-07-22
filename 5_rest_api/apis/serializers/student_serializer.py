from rest_framework import serializers

from apis.models.students import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
