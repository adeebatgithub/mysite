
from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", Dashboard_View.as_view(), name="dashboard"),
]
