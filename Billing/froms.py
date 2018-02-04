from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from . import models


class Record_Form(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = '__all__'
        widgets = {
            'transaction_time': AdminSplitDateTime()
        }
