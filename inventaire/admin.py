from django.contrib import admin
from .models import Objet

class ObjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_objet', 'quantite', 'description' ,'user')  # Affiche le nom, type, quantité et utilisateur
    list_filter = ('type_objet', 'user')  # Permet de filtrer par type d'objet et par utilisateur
    search_fields = ('nom', 'user__username')  # Recherche par nom d'objet et nom d'utilisateur

admin.site.register(Objet, ObjetAdmin)
