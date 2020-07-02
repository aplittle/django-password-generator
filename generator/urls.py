from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'generator_home'),
    path('password/', views.password, name = 'password'),
    path('about/', views.about, name = 'about'),
]
