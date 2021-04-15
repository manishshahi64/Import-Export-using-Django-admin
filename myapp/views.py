from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AdminView(TemplateView):
    template_name="admin.html"