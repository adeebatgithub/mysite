from django.shortcuts import render
from django.views import generic as gv
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class Signup_View(SuccessMessageMixin, gv.CreateView):
    
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
    context_object_name = "form"
    success_message = "signup successful"
    
class Test(gv.FormView, SuccessMessageMixin):
    
    template_name = "signup.html"
    success_massage = "success"
    form_class = UserCreationForm
    success_url = "/user/test"
    
def test(request):
    
    form = UserCreationForm
    
    if request.method == "POST":
        
        form = form(request.POST)
        
        for e in form.errors.values():
            print(dir(e))
        
    return render(request, "signup.html",{"form":form})
    
    