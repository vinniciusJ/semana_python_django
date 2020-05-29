from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def cadastrar_usario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)

        if form_usuario.is_valid():
            form_usuario.save()

            return redirect('listar_tarefas')
    else:
        form_usuario = UserCreationForm()

    return render(request, 'usuarios/form_usuario.html', {'form_usuario':form_usuario})

def logar_usuario(request):
    form_login = AuthenticationForm()

    return render(request, 'usuarios/form_login.html', {'form_login' : form_login})