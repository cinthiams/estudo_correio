from .views import Perfil,Rastreio
from django.urls import path,include
from . import views
urlpatterns = [
    #path('cadastro',Usuario.as_view(), name='cadastro'),
   
    
   
    path('perfil', Perfil.as_view(), name='perfil'),
    path('rastreio', views.Rastreio, name='rastreio'),
    
    
    
    
    
]
