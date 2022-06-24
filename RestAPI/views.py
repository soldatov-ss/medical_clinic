from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework import generics

from clinic_site.models import Specialist, Specialty
from .serialisers import SpecialtySerializer, SpecialistSerializer
from .service import SpecialistFilter


class SpecialistsListView(generics.ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'specialties__name']
    filterset_class = SpecialistFilter
    ordering_fields = ['work_experience', 'date_birth']


class SpecialtiesListView(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

