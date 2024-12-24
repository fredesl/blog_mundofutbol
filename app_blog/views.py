from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, PerfilAvatar
from .forms import BlogFormulario, RegistroForm, EditarPerfilForm, PerfilAvatarForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request, "app_blog/index.html")

@login_required(login_url="iniciar-sesion")
def formulario_blog(request):
    if request.method == "POST":
        form_blog = BlogFormulario(request.POST, request.FILES)

        if form_blog.is_valid():
            blog = form_blog.save(commit=False)
            blog.autor = request.user
            blog.save()
            return redirect('ver-posts')
    else:
        form_blog = BlogFormulario()
        return render(request,"app_blog/forms/blog-formulario.html",{"form_blog":form_blog})
    

def ver_posts(request):
    blogs = Blog.objects.all()
    return render(request, "app_blog/blogs.html",{"blogs":blogs})

@login_required(login_url="iniciar-sesion")
def blog_detalle(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "app_blog/blog-detalle.html",{"blog":blog})

@login_required
def blog_editar(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        form_blog = BlogFormulario(request.POST, instance=blog)
        if form_blog.is_valid():
            form_blog.save()
            return redirect("ver-posts")
    else:
        form_blog = BlogFormulario(instance=blog)
        return render(request, "app_blog/blog-editar.html", {"form_blog": form_blog})

@login_required    
def blog_eliminar(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("ver-posts")


def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio') 
        else:
            return redirect('inicio')
    return render(request, 'app_blog/login.html')

def registro_usuario(request):
    if request.method == "POST":
        form_registro = RegistroForm(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return redirect('inicio')
    else:
        form_registro = RegistroForm()
    
    return render(request, 'app_blog/registro.html', {"form_registro": form_registro})

@login_required 
def ver_perfil(request):
    usuario = request.user
    perfil, _ = PerfilAvatar.objects.get_or_create(usuario=usuario)
    return render(request, "app_blog/ver-perfil.html",{"perfil": perfil})

@login_required 
def editar_perfil(request):
    usuario = request.user
    perfil, _ = PerfilAvatar.objects.get_or_create(usuario=usuario)
    if request.method == "POST":
        form_editar = EditarPerfilForm(request.POST, instance=usuario)
        form_foto = PerfilAvatarForm(request.POST, request.FILES, instance=perfil)
        if form_editar.is_valid() and form_foto.is_valid():
            form_editar.save()
            form_foto.save()
            return redirect('ver-perfil')
        else:
            form_editar = EditarPerfilForm()
    else:
        form_editar = EditarPerfilForm(instance=usuario)
        form_foto = PerfilAvatarForm(instance=perfil)

    return render(request, "app_blog/forms/editar-perfil.html",{"form_editar":form_editar,"form_foto":form_foto})

@login_required
def cambiar_contrasena(request):
    usuario = request.user
    if request.method == "POST":
        form_contrasena = PasswordChangeForm(usuario,request.POST)
        if form_contrasena.is_valid():
            form_contrasena.save()
            return redirect('iniciar-sesion')
        else:
            return redirect('inicio') 
    else:
        form_contrasena = PasswordChangeForm(usuario)
    return render(request, "app_blog/forms/cambiar-contrasena.html",{"form_contrasena":form_contrasena})


def acerca_de(request):
    return render(request, "app_blog/acerca.html")
