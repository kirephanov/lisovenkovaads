from .models import Ads, Script
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    # Форма авторизации
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    # Форма регистрации
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=320, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AdsForm(ModelForm):
    # Форма для размещения рекламы
    class Meta:
        model = Ads
        fields = ['ads_url', 'ads_email', 'ads_category', 'ads_description', 'ads_image']

        widgets = {
            'ads_url': TextInput(attrs={
                'class': 'form-control',
                'id': 'ads_url',
            }),
            'ads_email': TextInput(attrs={
                'class': 'form-control',
                'id': 'ads_email',
            }),
            'ads_category': Select(attrs={
                'class': 'form-select',
                'id': 'ads_category',
            }),
            'ads_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'ads_description',
                'rows': '3',
            }),
            'ads_image': ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': "image/png, image/jpeg",
                'id': 'ads_image',
            }),
        } 


class ScriptForm(ModelForm):
    # Форма для получения скрипта
    class Meta:
        model = Script
        fields = ['script_url', 'script_email', 'script_category']

        widgets = {
            'script_url': TextInput(attrs={
                'class': 'form-control',
                'id': 'ads_url',
            }),
            'script_email': TextInput(attrs={
                'class': 'form-control',
                'id': 'ads_email',
            }),
            'script_category': Select(attrs={
                'class': 'form-select',
                'id': 'ads_category',
            }),
        }
