from django import forms
from django.core.exceptions import ValidationError
from .models import User

class RegisterForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmer le mot de passe')

    class Meta:
        model = User
        fields = ['user_login', 'email', 'user_password']  # Utiliser 'email' au lieu de 'user_mail'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('user_password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(label='Adresse email')
    user_password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user_password = cleaned_data.get('user_password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Utilisateur non trouvé")

        if not user.check_password(user_password):
            raise ValidationError("Mot de passe incorrect")

        cleaned_data['user'] = user
        return cleaned_data
