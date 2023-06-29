
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()



    class Meta:
        model = User
        fields = ['username', 'password1', 'last_name', 'email']