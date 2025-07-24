from django.db.models import Count
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.filters.school_filters import SchoolFilter
from apis.models.schools_model import Schools
from apis.serializers.base_serializer import SchoolSerializer
from apis.serializers.detail_serializer import SchoolDetailSerializer


@extend_schema(tags=["Schools"])
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = Schools.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolFilter

    def retrieve(self, request: Request, *args, **kwargs):
        queryset = Schools.objects.annotate(
            count_class_room=Count('classrooms', distinct=True),
            count_teacher=Count('classrooms__teachers', distinct=True),
            count_student=Count('classrooms__students', distinct=True),
        )
        pk = kwargs['pk']
        school = queryset.get(pk=pk)
        school_data = SchoolDetailSerializer(school).data
        return Response(data=school_data, status=status.HTTP_200_OK)
