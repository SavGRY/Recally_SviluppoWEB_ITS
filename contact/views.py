from sre_constants import SUCCESS
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from . import forms
from .forms import ContactForm


class ContactFormView(generic.CreateView):
    template_name='contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home_page')
    
    def form_valid(self, form):
        return super().form_valid(form)
