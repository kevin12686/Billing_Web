from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list.as_view(), name='record_list'),
    path('detail/<pk>', views.record_detail.as_view(), name='record_detail'),
    path('update/<pk>', views.record_update.as_view(), name='record_update'),
]
