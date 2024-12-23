from django.urls import path

from app_blog import views

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