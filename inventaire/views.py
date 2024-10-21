from django.shortcuts import render, get_object_or_404, redirect
from .models import Objet
from .forms import ObjetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


# Lister les objets de l'utilisateur connecté
@login_required
def objet_list(request):
    try:
        # Filtrer uniquement les objets appartenant à l'utilisateur connecté
        objets = Objet.objects.filter(user=request.user)
    except Objet.DoesNotExist:
        # S'assurer qu'aucun objet n'est trouvé pour cet utilisateur
        objets = []

    return render(request, 'inventaire/objet_list.html', {'objets': objets})


# Ajouter un nouvel objet à l'inventaire de l'utilisateur
@login_required
def objet_create(request):
    if request.method == 'POST':
        form = ObjetForm(request.POST)
        if form.is_valid():
            objet = form.save(commit=False)
            objet.user = User.objects.get(pk=request.user.pk)
            objet.save()
            return redirect('objet_list')
    else:
        form = ObjetForm()
    return render(request, 'inventaire/objet_form.html', {'form': form})

# Modifier un objet existant
def objet_update(request, pk):
    objet = get_object_or_404(Objet, pk=pk, user=request.user)  # Vérifier que l'objet appartient à l'utilisateur
    if request.method == 'POST':
        form = ObjetForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect('objet_list')
    else:
        form = ObjetForm(instance=objet)
    return render(request, 'inventaire/objet_form.html', {'form': form})


# Supprimer un objet
def objet_delete(request, pk):
    objet = get_object_or_404(Objet, pk=pk, user=request.user)  # Vérifier que l'objet appartient à l'utilisateur
    if request.method == 'POST':
        objet.delete()
        return redirect('objet_list')
    return render(request, 'inventaire/objet_confirm_delete.html', {'objet': objet})






