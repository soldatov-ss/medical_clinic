from django_filters import rest_framework as filters

from clinic_site.models import Doctor


class CharFieldInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class DoctorFilter(filters.FilterSet):
    specialties = CharFieldInFilter(field_name='specialties__name', lookup_expr='in')
    date_birth = filters.DateTimeFilter()
    work_experience = filters.RangeFilter()

    class Meta:
        model = Doctor
        fields = ('specialties', 'work_experience', 'number_of_sort')
