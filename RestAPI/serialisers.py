from rest_framework import serializers

from clinic_site.models import Specialty, Specialist


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('name', 'number_of_sort')


class SpecialistSerializer(serializers.ModelSerializer):
    specialties = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Specialist
        fields = ('name', 'number_of_sort', 'specialties', 'description', 'date_birth', 'work_experience')

