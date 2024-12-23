from django.shortcuts import render, redirect
from .models import Mensaje
from django.contrib.auth.models import User

def crear_mensaje(request):
    if request.method == "POST":
        destinatario_usuario = request.POST.get("destinatario")
        cuerpo_mensaje = request.POST.get("cuerpo_mensaje")
        destinatario = User.objects.get(username=destinatario_usuario)
        Mensaje.objects.create(remitente=request.user,destinatario=destinatario,cuerpo_mensaje=cuerpo_mensaje)
        return redirect("inicio")
    
    usuarios = User.objects.exclude(username=request.user.username)

    return render(request, 'app_mensajes/crear-mensaje.html',{"usuarios":usuarios})


def ver_mensajes(request):

    mensajes = Mensaje.objects.filter(destinatario=request.user)

    return render(request, 'app_mensajes/ver-mensajes.html',{"mensajes":mensajes})