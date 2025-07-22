from django.db import models

from apis.models.schools import Schools


class ClassRooms(models.Model):
    class_level = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

    class Meta:
        unique_together = [["school", "class_level", "room"]]
