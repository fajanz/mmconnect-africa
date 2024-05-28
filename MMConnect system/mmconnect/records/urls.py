# records/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_record, name='add_record'),
    path('', views.view_records, name='view_records'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
]
