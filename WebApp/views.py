from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class UserCreateView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('playlist:home')
    
    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username,password=password)
        login(self.request, user)
        return redirect(self.success_url)


def index(request):
    return render(request, 'index.html')


def privacy(request):
    return render(request, 'privacy.html', context={"year": datetime.now().year})
