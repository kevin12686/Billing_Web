from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list.as_view(), name='record_list'),
    path('record/detail/<pk>', views.record_detail.as_view(), name='record_detail'),
    path('record/update/<pk>', views.record_update.as_view(), name='record_update'),
    path('record/delete/<pk>', views.record_delete.as_view(), name='record_delete'),
    path('record/create/', views.record_create.as_view(), name='record_create'),
    path('account/', views.account_list.as_view(), name='account_list'),
    path('account/create/', views.account_create.as_view(), name='account_create'),
    path('account/update/<pk>', views.account_update.as_view(), name='account_update'),
    path('account/delete/<pk>', views.account_delete.as_view(), name='account_delete'),
]
