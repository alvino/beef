from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def logout(request):
    auth.logout(request)
    return redirect('/usuario/login')

def login(request):
    next = request.GET.get('next')
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":

        username = request.POST.get('inputUsername')
        senha = request.POST.get("inputPassword")
        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect(next or '/dashboard')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuario/login')


def register(request):
    if(request.method == 'POST'):
        username = request.POST.get('inputUsername')
        email = request.POST.get("inputEmail")
        senha = request.POST.get("inputPassword")
        confirmar_senha = request.POST.get('inputPasswordConfirm')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect('/usuario/register')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha deve ser iguais')
            return redirect('/usuario/register')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect('/usuario/register')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            return redirect('/usuario/login')
        except:
            print('Erro 4')
            return redirect('/usuario/register')
    else:
        return render(request, 'register.html')