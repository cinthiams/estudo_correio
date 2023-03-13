from .views import Perfil,Rastreio
from django.urls import path,include

urlpatterns = [
    #path('cadastro',Usuario.as_view(), name='cadastro'),
   
    
   
    path('perfil', Perfil.as_view(), name='Perfil'),
    path('rastreio', Rastreio.as_view(), name='rastreio'),
    
    
    
    
    
]
