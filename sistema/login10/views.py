from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
# Create your views here.

def home(request):
    return render(request, 'home.html')


#Authenticate
def registrate(request):
    if  request.method == 'GET':
        return render(request, './login/registrate.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('home')
        else:
            return render(request, './login/registrate.html',{
            'form': UserCreationForm,
            'error':'las contrasenias no coinsiden'
            
        })

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, './login/iniciar_sesion.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, './login/iniciar_sesion.html',{
                'form':AuthenticationForm,
                'error':'La cuenta no se ah encontrado la cuenta'
        })
        else:
            login(request,user)
            return redirect('home')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')