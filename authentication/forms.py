from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ModelForm, TextInput, Textarea

# sign_up.html -- POST
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        fields = ["email", "password"]
        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input email"
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input password"
            }),
        }

# change_user.html -- PUT
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = ["email", "password"]
        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input email"
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input password"
            }),
        }
