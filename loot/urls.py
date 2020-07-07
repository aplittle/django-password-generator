from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'loot_home'),
]
