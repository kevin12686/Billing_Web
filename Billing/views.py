from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from . import models


# Create your views here.

class record_list(ListView):
    model = models.Record
    ordering = 'transaction_time'
    template_name = 'record_list.html'


class record_detail(DetailView):
    model = models.Record
    template_name = 'record_detail.html'


class record_update(UpdateView):
    model = models.Record
    fields = ['transaction_time', 'record_type', 'amount', 'fee']
    template_name = 'record_form.html'

    def get_success_url(self):
        messages.success(self.request, '更新成功')
        return reverse('record_list')
