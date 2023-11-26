from django.shortcuts import render
from django.views import View
from django.views import generic as gv
from django.contrib.auth.mixins import LoginRequiredMixin

class Index_View(LoginRequiredMixin, gv.RedirectView):
    
    url = "/todo/dashboard"

class Dashboard_View(LoginRequiredMixin, gv.TemplateView):

    template_name = "dashboard.html"