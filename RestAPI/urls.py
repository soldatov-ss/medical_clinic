from django.urls import path

from . import views

urlpatterns = [
    path('specialists/', views.SpecialistsListView.as_view()),
    # path('specialists/<slug:slug>/', views.SpecialistUpdateView.as_view()),
    path('specialties/', views.SpecialtiesListView.as_view()),
]