from rest_framework import serializers

from apis.models.schools import Schools


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = "__all__"
