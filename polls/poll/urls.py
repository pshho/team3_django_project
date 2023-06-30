
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index_search, name='map_search'),
    path('index_search_list/', views.index_search_list, name='index_search_list'),
    path('test/', views.test_socal, name='test'),
]
