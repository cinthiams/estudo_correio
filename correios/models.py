from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField

# Create your models here.

class Base(models.Model):
  publicacao = models.DateTimeField(auto_now_add=True)
  atualização = models.DateTimeField(auto_now=True)
  ativo = models.BooleanField(default=True)
  class Meta:
    abstract = True 

class Endereco(Base):
  blank_choice = (('', '---------'),)

  cep = models.CharField(max_length=100)
  rua = models.CharField(max_length=200)
  bairro = models.CharField(max_length=200)
  numero = models.IntegerField(max_length=200)
  cidade =  models.CharField(
    max_length=100, choices=blank_choice, blank=False, null=False, default=''
   )
  estado = models.CharField(
    max_length=100, choices=blank_choice, blank=False, null=False, default=''
   )
  complemento = models.CharField(max_length=70)

class Encomenda(Base):
  codigo = models.CharField(max_length=100)
  status = models.BooleanField(default=True)
  
class Usuario(Base):
  usuario =  models.OneToOneField(User, on_delete=models.CASCADE)
  encomendas = models.ManyToManyField(Encomenda,null=True)
  endereco = models.ManyToManyField(Endereco,null= True)
  foto = StdImageField('foto', upload_to='path/to/img', null=True)
  def __str__(self):
    return "{}".format(self.usuario.username, self.usuario.password, self.usuario.email, self.usuario.groups,self.encomendas)