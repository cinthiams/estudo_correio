from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UsuarioForm
from django.views.generic.base import TemplateView
import requests
import json
from api import url
from django.http import HttpResponse
from django.template import loader

class Login(TemplateView):
  template_name  = "login.html"

class Registro(TemplateView):
  template_name  = "registro.html"

class Endereco(TemplateView):
  template_name  = "endereco.html"


class Perfil(TemplateView):
  template_name  = "perfil.html" 


 
def Rastreio(request):
  template = loader.get_template('rastreio.html')
  if request.method =='GET':
    
    teste = requests.get(url)
    todos = json.loads(teste.content)
    print(todos['codigo'],'informaçoes',todos['eventos'][0]['status'])
    for i in todos['eventos']:
      print(i['status'])
    context = {
      'status': todos['eventos'][0]['status'],
      
    }
    return HttpResponse(template.render(context, request))
    
  return render(request,'rastreio.html')