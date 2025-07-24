from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.models.classrooms_model import ClassRooms
from apis.serializers.base_serializer import ClassRoomSerializer
from apis.serializers.detail_serializer import ClassRoomDetailSerializer


@extend_schema(tags=["Class Rooms"])
class ClassRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = ClassRoomSerializer
    queryset = ClassRooms.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        pk = kwargs['pk']
        class_room = ClassRooms.objects.prefetch_related('teachers', 'students').get(pk=pk)
        class_room_data = ClassRoomDetailSerializer(class_room).data
        return Response(data=class_room_data, status=status.HTTP_200_OK)
