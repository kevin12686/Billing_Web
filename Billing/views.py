from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, FormView

from . import models, froms


# Create your views here.

class record_list(ListView):
    model = models.Record
    ordering = 'transaction_date'
    template_name = 'record_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_form'] = froms.Record_Form()
        return context


class record_detail(DetailView):
    model = models.Record
    template_name = 'record_detail.html'


class record_create(CreateView):
    form_class = froms.Record_Form
    template_name = 'record_form.html'

    def get_success_url(self):
        messages.success(self.request, '建立成功')
        return reverse('record_list')


class record_update(UpdateView):
    form_class = froms.Record_Form
    template_name = 'record_form.html'

    def get_success_url(self):
        messages.success(self.request, '更新成功')
        return reverse('record_list')
