from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView

from . import models


# Create your views here.

class record_list(ListView):
    model = models.Record
    template_name = 'record_list.html'
