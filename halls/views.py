from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'halls/home.html')

class Signup(generic.CreateView):
    form_class = UserCreationForm
    sucess_url = reverse_lazy('home')
    template_name = 'registration/signup.html'