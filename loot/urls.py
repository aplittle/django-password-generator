from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'loot_home'),
    path('addloot.html/', views.addloot, name = 'add_loot'),
    path('addnewloot.html/', views.addnewloot, name='add_new_loot'),
]
