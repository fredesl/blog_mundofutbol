from django.urls import path
from .views import crear_mensaje, ver_mensajes

urlpatterns = [
    path('crear-mensaje/', crear_mensaje, name="crear-mensaje"),
    path('ver-mensajes/', ver_mensajes, name="ver-mensajes"),
]