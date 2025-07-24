from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1.class_rooms_viewset import ClassRoomsViewSet
from apis.views.v1.school_viewset import SchoolViewSet
from apis.views.v1.student_viewset import StudentViewSet
from apis.views.v1.teacher_viewset import TeacherViewSet

router = DefaultRouter()

router.register(r"schools", SchoolViewSet, basename="schools")
router.register(r"class-rooms", ClassRoomsViewSet, basename="class-rooms")
router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"students", StudentViewSet, basename="students")

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
