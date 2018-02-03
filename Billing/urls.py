from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list.as_view(), name='record_list'),
]
