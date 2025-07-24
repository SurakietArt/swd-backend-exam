from django.contrib import admin

from apis.models.classrooms_model import ClassRooms
from apis.models.schools_model import Schools
from apis.models.students_model import Students
from apis.models.teachers_model import Teachers

# Register your models here.
admin.site.register(Schools)
admin.site.register(ClassRooms)
admin.site.register(Students)
admin.site.register(Teachers)
