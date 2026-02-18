from django.urls import path
from . import views

app_name = 'journal'

urlpatterns =[
    path('', views.Home, name='home'),
    path('entries/', views.EntryList, name='entry_list'),
    path('entry-details/<int:pk>/', views.EntryDetail, name='entry_detail'),
    path('entry-create/', views.EntryCreate.as_view(), name='entry_create'),
    path('entry-update/<int:pk>/', views.EntryUpdate.as_view(), name='entry_update'),
    path('entry-delete/<int:pk>/', views.EntryDelete.as_view(), name='entry_delete'),
]