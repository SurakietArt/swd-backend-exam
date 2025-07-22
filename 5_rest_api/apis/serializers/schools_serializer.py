from rest_framework import serializers

from apis.models.schools import Schools


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = "__all__"


class SchoolDetailSerializer(serializers.ModelSerializer):
    count_class_room = serializers.IntegerField(read_only=True)
    count_teacher = serializers.IntegerField(read_only=True)
    count_student = serializers.IntegerField(read_only=True)

    class Meta:
        model = Schools
        fields = "__all__"
