from django.urls import path
from . import views

app_name = 'journal'

urlpatterns =[
    path('', views.Home, name='home'),
    path('entries/', views.EntryList, name='entry_list'),
]