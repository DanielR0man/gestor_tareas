# tareas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('nueva/', views.nueva_tarea, name='nueva_tarea'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('clasificar/<str:categoria>/', views.clasificar_tareas, name='clasificar_tareas'),
    path('detalle/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
]
