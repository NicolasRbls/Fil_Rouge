from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Les champs à afficher dans la liste
    list_display = ('email', 'user_login', 'is_staff', 'user_date_new')

    # Les champs à utiliser lors de la modification d'un utilisateur dans l'admin
    fieldsets = (
        (None, {'fields': ('email', 'user_login', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    # Exclure les champs non modifiables du formulaire d'ajout et de modification
    readonly_fields = ['user_date_new']

    # Les champs à utiliser lors de la création d'un nouvel utilisateur dans l'admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_login', 'password1', 'password2'),
        }),
    )

    # Tri par défaut
    ordering = ('email',)
