from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="enviados", on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name="recibidos", on_delete=models.CASCADE)
    cuerpo_mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"De: {self.remitente} para: {self.destinatario}"


