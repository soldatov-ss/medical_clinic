from django.contrib import admin

from .models import Specialist, Specialty


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'number_of_sort')}
    list_display = ("id", "number_of_sort", "name", 'get_specialties')
    list_filter = ('name', 'number_of_sort', 'specialties__name', 'date_birth', 'work_experience')
    search_fields = ('name', 'specialties__name', 'number_of_sort')
    list_display_links = ('name', 'number_of_sort')
    save_on_top = True

    def get_specialties(self, obj):
        return ", ".join([p.name for p in obj.specialties.all()])


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'number_of_sort')}
    list_display_links = ('name',)
    list_display = ("id", "name", 'number_of_sort')
    list_filter = ('name', 'number_of_sort')
    search_fields = ('name',)
