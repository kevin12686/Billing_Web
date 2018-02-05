from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from . import models, forms


# Create your views here.

class record_list(ListView):
    model = models.Record
    ordering = 'transaction_date'
    template_name = 'record_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_form'] = forms.Record_Form()
        context['total_expend'] = sum(
            [each.amount for each in self.model.objects.filter(record_type=models.Record.EXPEND)])
        context['total_income'] = sum(
            [each.amount for each in self.model.objects.filter(record_type=models.Record.INCOME)])
        context['balance'] = context['total_income'] - context['total_expend']
        return context


class record_create(CreateView):
    form_class = forms.Record_Form
    template_name = 'record_form.html'

    def get_success_url(self):
        messages.success(self.request, '建立成功')
        return reverse('record_list')


class record_update(UpdateView):
    model = models.Record
    form_class = forms.Record_Form
    template_name = 'record_form.html'

    def get_success_url(self):
        messages.success(self.request, '更新成功')
        return reverse('record_list')


class record_detail(DetailView):
    model = models.Record
    template_name = 'record_detail.html'


class record_delete(DeleteView):
    model = models.Record
    template_name = 'delete_conform.html'

    def get_success_url(self):
        messages.success(self.request, '刪除成功')
        return reverse('record_list')


class account_list(ListView):
    model = models.Account
    template_name = 'account_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_form'] = forms.Account_Form()
        return context


class account_create(CreateView):
    form_class = forms.Account_Form
    template_name = 'account_form.html'

    def form_valid(self, form):
        form.instance.balance = form.instance.initial_amount
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, '建立成功')
        return reverse('account_list')


class account_update(UpdateView):
    model = models.Account
    form_class = forms.Account_Form
    template_name = 'account_form.html'

    def form_valid(self, form):
        oid_initial_amount = self.get_object().balance
        form.instance.balance += form.instance.initial_amount - oid_initial_amount
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, '更新成功')
        return reverse('account_list')


class account_detail(DetailView):
    model = models.Account


class account_delete(DeleteView):
    model = models.Account
    template_name = 'delete_conform.html'

    def get_success_url(self):
        messages.success(self.request, '刪除成功')
        return reverse('account_list')
