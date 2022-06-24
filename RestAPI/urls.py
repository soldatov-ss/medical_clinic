from django.urls import path

from . import views

urlpatterns = [

    path('doctors/', views.DoctorsListView.as_view()),
    path('specialties/', views.SpecialtiesListView.as_view()),
    path('doctors/create/', views.CreateDoctorView.as_view()),
    path('specialties/create/', views.CreateSpecialtyView.as_view()),
    path('specialties/<slug:slug>/', views.EditSpecialtyView.as_view()),
    path('doctors/<slug:slug>/', views.EditDoctorView.as_view()),
]
