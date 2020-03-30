from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_ingredient', views.add_ingredient),
    path('reset', views.reset),  
]