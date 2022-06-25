from rest_framework import serializers

from clinic_site.models import Specialty, Doctor


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('name', 'number_of_sort')


class DoctorsSerializer(serializers.ModelSerializer):
    specialties = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ('name', 'number_of_sort', 'specialties', 'description', 'date_birth', 'work_experience')


class EditDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'number_of_sort', 'specialties', 'description', 'date_birth', 'work_experience')
