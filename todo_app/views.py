from django.shortcuts import render
from django.views import View
from django.views import generic as gv
from django.contrib.auth import mixins as mx

class Index_View(mx.LoginRequiredMixin, gv.RedirectView):
    
    url = "/todo/dashboard"