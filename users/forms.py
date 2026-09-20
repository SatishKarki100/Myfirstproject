from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=255,required=True)
    first_name = forms.CharField(max_length=100, required=True)
    middlename = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        User=get_user_model()
        model = User 
        fields = ['username','first_name', 'middlename', 'last_name', 'email']

