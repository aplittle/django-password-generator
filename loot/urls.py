from django.urls import path
from . import views

urlpatterns = [
    path('', views.loot_home, name = 'loot_home'),
]
