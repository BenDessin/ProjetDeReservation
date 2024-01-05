from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ProfilUser
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = ProfilUser
        fields = ("nom", "prenom", "telephone", "email", "password1",)
        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control'}),
            'prenom' : forms.TextInput(attrs={'class':'form-control'}),
            'telephone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'Password1' : forms.TextInput(attrs={'class':'form-control'})
        }

class AuthForm(AuthenticationForm):
    class Meta:
        widget = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }