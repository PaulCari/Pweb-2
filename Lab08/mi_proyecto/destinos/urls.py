from django.urls import path
from . import views
from .views import generar_pdf

urlpatterns = [
    path('', views.listar_destinos, name='listar_destinos'),
    path('añadir/', views.añadir_destino, name='añadir_destino'),
    path('modificar/<int:id>/', views.modificar_destino, name='modificar_destino'),
    path('eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
     path('generar_pdf/', generar_pdf, name='generar_pdf'),
]

