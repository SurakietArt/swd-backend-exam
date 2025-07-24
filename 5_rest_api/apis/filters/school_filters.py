import django_filters

from apis.models.schools_model import Schools


class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Schools
        fields = ['name']
