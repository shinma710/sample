"""This is a test program."""
from django.urls import path
from . import views

app_name = 'sample_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('question/', views.question, name='question'),
]