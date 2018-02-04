from django import forms
from . import models


class Record_Form(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = '__all__'
