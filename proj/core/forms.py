from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter your username","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter your password","class":'w-full py-4 px-6 rounded-xl'}), required=True)

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        # fields
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter your username","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':"Enter your email","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter your password","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Repeat password","class":'w-full py-4 px-6 rounded-xl'}), required=True)
