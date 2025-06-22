from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:pk>/', views.visualizar_usuario, name='visualizar_usuario'),
    path('usuarios/novo/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario')
]