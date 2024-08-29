from typing import Any
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "photo"]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields.pop('password_based_authentication',None)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')