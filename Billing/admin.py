from django.contrib import admin

from .models import Record, Account

# Register your models here.

admin.site.register(Account)
admin.site.register(Record)
