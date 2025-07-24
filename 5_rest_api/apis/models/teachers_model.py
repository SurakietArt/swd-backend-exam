from django.db import models

from apis.enums.enums import Sex
from apis.models.classrooms_model import ClassRooms


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(
        max_length=10,
        choices=Sex.choices,
    )
    class_room = models.ManyToManyField(ClassRooms, related_name="teachers")
