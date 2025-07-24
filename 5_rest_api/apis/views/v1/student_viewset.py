from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.models.students_model import Students
from apis.serializers.base_serializer import TeacherSerializer
from apis.serializers.detail_serializer import StudentDetailSerializer


@extend_schema(tags=["Students"])
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Students.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        pk = kwargs['pk']
        student = Students.objects.prefetch_related('class_room').get(pk=pk)
        student_data = StudentDetailSerializer(student).data
        return Response(data=student_data, status=status.HTTP_200_OK)
