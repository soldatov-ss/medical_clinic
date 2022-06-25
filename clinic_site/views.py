from django.views.generic import UpdateView, TemplateView
from rest_framework.generics import ListAPIView


class UpdatePostView(TemplateView):
    template_name = 'clinic_site/index.html'
