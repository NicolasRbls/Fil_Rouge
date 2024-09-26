from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['user_login', 'user_mail', 'user_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('user_password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=255, label='Login')
    user_password = forms.CharField(widget=forms.PasswordInput, label='Password')
