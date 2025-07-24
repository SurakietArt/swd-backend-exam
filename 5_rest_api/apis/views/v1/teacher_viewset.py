from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.filters.teacher_filter import TeacherFilter
from apis.models.teachers_model import Teachers
from apis.serializers.base_serializer import TeacherSerializer
from apis.serializers.detail_serializer import TeacherDetailSerializer


@extend_schema(tags=["Teachers"])
class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeacherFilter

    def retrieve(self, request: Request, *args, **kwargs):
        pk = kwargs['pk']
        teacher = Teachers.objects.prefetch_related('class_room').get(pk=pk)
        teacher_data = TeacherDetailSerializer(teacher).data
        return Response(data=teacher_data, status=status.HTTP_200_OK)
