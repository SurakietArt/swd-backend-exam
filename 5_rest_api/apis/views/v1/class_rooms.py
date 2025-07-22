from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from apis.models.classrooms import ClassRooms
from apis.serializers.class_room_serializer import ClassRoomSerializer, ClassRoomDetailSerializer


class ClassRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = ClassRoomSerializer
    queryset = ClassRooms.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        class_room = self.get_object()
        class_room_data = ClassRoomDetailSerializer(class_room).data
        return Response(data=class_room_data, status=status.HTTP_200_OK)
