
from django.urls import path,include
from .views import *

urlpatterns = [
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup", Signup_View.as_view(), name="signup"),
    
    path("Test", Test.as_view()),
    path("test", test)
]
