from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.models.schools import Schools
from apis.serializers.schools_serializer import SchoolSerializer, SchoolDetailSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = Schools.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        queryset = Schools.objects.annotate(
            count_class_room=Count('classrooms', distinct=True),
            count_teacher=Count('classrooms__teachers', distinct=True),
            count_student=Count('classrooms__students', distinct=True),
        )
        school = queryset.get(pk=kwargs['pk'])
        school_data = SchoolDetailSerializer(school).data
        return Response(data=school_data, status=status.HTTP_200_OK)
