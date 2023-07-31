from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


# ====================================================(All forms of the videos are below)

class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ('name', 'slug', 'prev', 'video')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text', 'type': 'text', 'placeholder': 'name'}),
            'slug': forms.TextInput(attrs={'class': 'text', 'type': 'text', 'placeholder': 'slug'}),
            'prev': forms.FileInput(attrs={'class': 'file', 'type': 'file'}),
            'video': forms.FileInput(attrs={'class': 'file', 'type': 'file'})
        }


# =================================================================================(All forms of the Profile are below)

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Ім'я", widget=forms.TextInput(attrs={'class': 'text',
                                                                           'placeholder': 'login'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text',
                                                                                  'placeholder': 'password1'}))
    password2 = forms.CharField(label='Повтор паролю', widget=forms.PasswordInput(attrs={'class': 'text',
                                                                                         'placeholder': 'password2'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'text',
                                                                           'placeholder': 'login'}))
    password = forms.CharField(label='pass', widget=forms.PasswordInput(attrs={'class': 'text',
                                                                               'placeholder': 'password'}))
