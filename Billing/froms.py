from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from . import models


class Record_Form(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = '__all__'
        widgets = {
            'transaction_date': AdminDateWidget()
        }
