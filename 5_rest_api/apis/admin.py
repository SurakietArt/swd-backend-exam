from django.contrib import admin

from apis.models.classrooms import ClassRooms
from apis.models.schools import Schools
from apis.models.students import Students
from apis.models.teachers import Teachers

# Register your models here.
admin.site.register(Schools)
admin.site.register(ClassRooms)
admin.site.register(Students)
admin.site.register(Teachers)
