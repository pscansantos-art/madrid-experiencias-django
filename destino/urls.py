from django.urls import path
from . import views

urlpatterns = [
    path('', views.atracoes, name='atracoes'),
    path('historia-cultura/', views.historia_cultura, name='historia_cultura'),
    path('galeria/', views.galeria, name='galeria'),
]