Mundo Fútbol
______________________________________________________________________________________________________________________________________________________________________
Descripción

Mundo Fútbol es un blog dedicado a brindar información sobre el fútbol argentino. El sitio permite a los administradores crear, editar y eliminar publicaciones relacionadas con el deporte. Los usuarios registrados pueden iniciar sesión para visualizar el contenido completo, interactuar con otros usuarios mediante mensajes privados, y personalizar su perfil.

Características

•	Gestión de publicaciones: Solo el administrador puede crear, editar o eliminar publicaciones.
•	Usuarios registrados: Los usuarios deben registrarse e iniciar sesión para acceder al contenido completo del blog.
•	Mensajes privados: Los usuarios pueden enviar y recibir mensajes privados entre ellos.
•	Perfiles personalizados: Los usuarios pueden agregar una foto a su perfil y actualizar su información personal.

Tecnologías utilizadas

•	Lenguaje principal: Python

•	Framework web: Django
•	Bases de datos: SQLite (por defecto)
•	Frontend: HTML5, CSS3, Bootstrap

Estructura del proyecto

El proyecto se llama proyecto_blog y cuenta con las siguientes aplicaciones principales:

1. app_blog
Modelos principales:

Blog: Modelo que representa las publicaciones del blog.

class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)
    etiqueta = models.CharField(max_length=30)

PerfilAvatar: Modelo para almacenar la foto de perfil de los usuarios.

class PerfilAvatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
URLs principales:

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    
    path("acerca-de-nosotros/", views.acerca_de, name="acerca-de-nosotros"),
    
    path("crear-post/", views.formulario_blog, name="crear-post"),
    
    path("ver-posts/", views.ver_posts, name="ver-posts"),
    
    path("blog-detalle/<int:id>", views.blog_detalle, name="blog-detalle"),
    
    path("blog-editar/<int:id>", views.blog_editar, name="blog-editar"),
    
    path("blog-eliminar/<int:id>", views.blog_eliminar, name="blog-eliminar"),
    
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar-sesion'),
    
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar-sesion'),
    
    path('registrarse/', views.registro_usuario, name='registrarse'),
    
    path('ver-perfil/', views.ver_perfil, name='ver-perfil'),
    
    path('editar-perfil/', views.editar_perfil, name='editar-perfil'),
    
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar-contrasena'),
    
]

2. app_mensajes
   
Modelo principal:

Mensaje: Modelo para gestionar los mensajes privados entre usuarios.

class Mensaje(models.Model):

    remitente = models.ForeignKey(User, related_name="enviados", on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name="recibidos", on_delete=models.CASCADE)
    cuerpo_mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    
URLs principales:

urlpatterns = [

    path('crear-mensaje/', crear_mensaje, name="crear-mensaje"),
    
    path('ver-mensajes/', ver_mensajes, name="ver-mensajes"),
    
]
_________________________________________________________________________________________________________________________________________________________________
Configuración inicial

1.	Clona este repositorio:
git clone https://github.com/fredesl/blog_mundofutbol.git

2.	Instala las dependencias requeridas:
pip install -r requirements.txt

3.	Realiza las migraciones iniciales:
python manage.py migrate

4.	Crea un superusuario:
python manage.py createsuperuser

5.	Inicia el servidor de desarrollo:
python manage.py runserver
_________________________________________________________________________________________________________________________________________________________________
Instrucciones de uso

1.	Ingresa al sitio como administrador para gestionar publicaciones.
2.	Los usuarios deben registrarse para acceder a las funcionalidades completas, como visualizar publicaciones y enviar mensajes.
3.	Los usuarios pueden personalizar su perfil agregando una foto y actualizando su información personal.
_________________________________________________________________________________________________________________________________________________________________
Autor
Leonardo Fredes
•	Correo: leonardomfredes@gmail.com
