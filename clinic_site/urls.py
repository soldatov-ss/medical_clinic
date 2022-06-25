from django.contrib import admin
from django.urls import path

from clinic_site.views import UpdatePostView

urlpatterns = [
    path('', UpdatePostView.as_view())
]