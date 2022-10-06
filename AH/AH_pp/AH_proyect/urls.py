from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('Iniciar_sesion', views.Iniciar_sesion, name='Iniciar_sesion'),
]
