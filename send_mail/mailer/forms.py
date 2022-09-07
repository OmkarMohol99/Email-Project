
from django import forms
from .models import Email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
