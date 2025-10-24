from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm  

class UserRegisterForm(UserCreationForm):
    class Meta:
        modem=User
        fields=['username','first_name','last_name','email','affiliation','nationality','password1','password2']
        widgets={
            'email':forms.EmailInput(attrs={'placeholder':"entrer votre email Universitaire",}),
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput(),
        }
