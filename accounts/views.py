from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from inventaire.models import Objet
from django.contrib.auth import authenticate, login


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Ne pas encore sauvegarder l'utilisateur
            user.set_password(form.cleaned_data['user_password'])  # Hache le mot de passe
            user.save()  # Sauvegarde de l'utilisateur
            messages.success(request, "Inscription réussie ! Vous pouvez vous connecter.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['user_password']
            user = authenticate(request, username=email, password=password)  # Utilisation de username=email
            if user is not None:
                if user.is_active:  # Vérifie que l'utilisateur est actif
                    login(request, user)
                    messages.success(request, f"Bienvenue {user.user_login}")
                    return redirect('home')
                else:
                    messages.error(request, "Votre compte est inactif.")
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def home_view(request):
    # Filtrer les objets en fonction de l'utilisateur connecté
    if request.user.is_authenticated:
        objets = Objet.objects.filter(user=request.user)  # Seuls les objets de l'utilisateur connecté
    else:
        objets = []  # Aucun objet si l'utilisateur n'est pas connecté

    return render(request, 'inventaire/objet_list.html', {'objets': objets})


