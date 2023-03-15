from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User, Group
from django.contrib import messages
from correios.models import Usuario
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserForms


def login_user(request):
  if request.method == 'POST': 
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    #grupo = get_object_or_404(Group, name="clientes")
    #print(username == '' ,'------------------------------------------------')
    if username == '' or password =='':
      messages.success(request,'informe o usuario e senha')
      return redirect('login')
      
    if user is not None:
      login(request,user)
      print(user,'------------DSADSAD----------------')
      return redirect('perfil')
          # Redirect to a success page.
    
    else:
      messages.success(request,'Usuario não cadastrado')
      return redirect('login')
     
          # Return an 'invalid login' error message.
  else:
    return render(request,'login.html')    

def logout_user(request):
  logout(request)
  messages.success(request,'Até logo!')
  return redirect('login')
#---------------------------------------------------------------------------------------------------------------------------------

  

def register_user(request,**args):
  new_group = Group.objects.get( name="clientes")
  if request.method =='POST':
    username1 = request.POST.get('username')
    email1 = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
  
    try:
      
      if password1 != password2:
        print('senha incorreta')
        messages.success(request,'senha diferente da outra')
        return redirect('registro')
      if User.objects.filter(email=email1).exists():
        messages.success(request,'usuario já existe')
        print('usuario já existeeeeeeeeeeeeeeeeeeeeeeeee')
        return redirect('registro')
      try:
        user = User.objects.get_or_create(username=username1, email=email1, password=password1, commit = False)
        user.groups.add(new_group)
        user.save()
  
        
        return redirect('perfil')
      except:
       
        messages.error(request,"usuario não salvo -------------------------------")
    except:
      messages.error(request,"usuario não definido")
      return render(request,'registro.html') 

  return render(request,'registro.html') 


def register_address(request):
  usuario = Usuario.objects.get()
  if request.method == 'POST': 
       context= {
                    'rua': usuario.endereco.rua,
                    'bairro': usuario.endereco.bairro,
                    'cep': usuario.endereco.cep,
                    'numero': usuario.endereco.numero
                    #'cidade': usuario.endereco.cidade
                    } 
       
     
  return render(request,'endereco.html')

  
  
"""  if form.is_valid():
      form.add(grupo)
      form.save()
  
      print(form,'-------------------nn------------------------------------------')
      #user = authenticate(username=username, password = password)
      messages.success('Usuario cadastrado! Faça login!')
      redirect('login')
        
  else:
    form = UserCreationForm()
  print('----------------------------------------------------------------')
  return render(request,'registro.html',{'form':form})"""


"""def register_user(request,**args):
  new_group = Group.objects.get_or_create(name = 'clientes')
  #form = createUserForms(request.POST)
  if request.method =='POST':
    username1 = request.POST.get('username')
    email1 = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    try:
      
      if password1 != password2:
        print('senha incorreta')
        messages.success(request,'senha diferente da outra')
        return redirect('registro')
      if User.objects.filter(email=email1).exists():
        messages.success(request,'usuario já existe')
        print('usuario já existeeeeeeeeeeeeeeeeeeeeeeeee')
        return redirect('registro')
      try:
        print('--------------------------------------------------------')
        user = User.objects.create(username=username1, email=email1, password=password1, commit = False)
        user.groups.add(new_group)
          
        user.save()
        messages.success("usuario criado com sucesso")
        print('user criado com sucessooooooooooooooooooo')
        return redirect(request,'endereco')
      except:
        messages.error(request,"usuario não salvo -------------------------------")
    except:
      messages.error(request,"usuario não definido")
      return render(request,'registro.html') 

      
    #else:  cinn123@gmail.com cinn3
    #  form = UserCreationForm()
  return render(request,'registro.html') 

  """