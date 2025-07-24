import django_filters

from apis.models.classrooms_model import ClassRooms


class ClassRoomFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    school_name = django_filters.CharFilter(field_name="school__name", lookup_expr="icontains")

    class Meta:
        model = ClassRooms
        fields = ['school_id', 'school_name']
