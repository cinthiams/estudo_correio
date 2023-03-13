from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UsuarioForm
from django.views.generic.base import TemplateView


class Login(TemplateView):
  template_name  = "login.html"

class Registro(TemplateView):
  template_name  = "registro.html"

class Endereco(TemplateView):
  template_name  = "endereco.html"


class Perfil(TemplateView):
  template_name  = "perfil.html" 


class Rastreio(TemplateView):
  template_name  = "rastreio.html" 

 
 