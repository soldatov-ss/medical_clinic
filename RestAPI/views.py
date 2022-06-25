from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics

from clinic_site.models import Doctor, Specialty
from .serialisers import SpecialtySerializer, DoctorsSerializer, EditDoctorSerializer
from .service import DoctorFilter


###########
# Лікарі
###########
class DoctorsListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'specialties__name']
    filterset_class = DoctorFilter
    ordering_fields = ['work_experience', 'date_birth']


class CreateDoctorView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = EditDoctorSerializer


class EditDoctorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditDoctorSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Doctor.objects.filter(slug=self.kwargs['slug'])
        return queryset


###########
# Напрямки
###########

class EditSpecialtyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialtySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Specialty.objects.filter(slug=self.kwargs['slug'])
        return queryset


class SpecialtiesListView(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['number_of_sort']


class CreateSpecialtyView(generics.CreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
