from django import forms
from .models import Blog, PerfilAvatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogFormulario(forms.ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ['autor']

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class EditarPerfilForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class PerfilAvatarForm(forms.ModelForm):

    class Meta:
        model = PerfilAvatar
        fields = ["foto"]