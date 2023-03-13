from .views import *
from django.urls import path,include
from . import views
urlpatterns = [
    #path('cadastro',Usuario.as_view(), name='cadastro'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('r', views.register_user, name='registro'),
    path('endereco', views.register_address, name='endereco')
 
    
    
]