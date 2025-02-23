from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class RegistaritionForm(UserCreationForm):
    email = forms.EmailField(required=True)
    code= forms.CharField(max_length=6)
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2',"code")