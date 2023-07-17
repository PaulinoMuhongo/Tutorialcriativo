from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    Novo_usuario = Usuario()
    Novo_usuario.Nome = request.POST.get('Nome')
    Novo_usuario.Idade = request.POST.get('Idade')
    Novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)