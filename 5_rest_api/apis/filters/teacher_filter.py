import django_filters

from apis.enums.enums import Sex
from apis.models.teachers_model import Teachers


class TeacherFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name="class_room__school__id", lookup_expr="exact")
    school_name = django_filters.CharFilter(field_name="class_room__school__name", lookup_expr="icontains")

    class_room_id = django_filters.NumberFilter(field_name="class_room__id", lookup_expr="exact")
    class_room_class_level = django_filters.CharFilter(field_name="class_room__class_level", lookup_expr="icontains")
    class_room = django_filters.CharFilter(field_name="class_room__room", lookup_expr="icontains")

    name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    sex = django_filters.ChoiceFilter(choices=Sex, lookup_expr="exact")

    class Meta:
        model = Teachers
        fields = [
            'school_id',
            'school_name',
            'class_room_id',
            'class_room_class_level',
            'class_room',
            'name',
            'last_name',
            'sex'
        ]
