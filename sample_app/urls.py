"""This is a test program."""
from django.urls import path
from . import views

app_name = 'sample_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('about/', views.about, name='about'),
    # path('info/', views.info, name='info'),
    path('sample_app/<int:pk>/', views.DetailView.as_view(), name='question'),
    path('sample_app/<int:pk>/plot', views.get_svg, name='plot'),
]