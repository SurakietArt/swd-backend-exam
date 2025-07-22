from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1.class_rooms import ClassRoomsViewSet
from apis.views.v1.school import SchoolViewSet

router = DefaultRouter()

router.register(r"schools", SchoolViewSet, basename="schools")
router.register(r"class-rooms", ClassRoomsViewSet, basename="class-rooms")
api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
