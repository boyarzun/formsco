# Django
from django.shortcuts import render

# CCBV
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "pages/home.html"
