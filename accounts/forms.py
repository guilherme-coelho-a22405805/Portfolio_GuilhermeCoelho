from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistoForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(label = "Nome", required=True)
  last_name = forms.CharField(label = "Sobrenome", required= True)

  class Meta:
    model = User
    fields = ['username','password1','password2','email','first_name','last_name']