from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

from django import forms

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True, label='メールアドレス')
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'password1', 'password2')