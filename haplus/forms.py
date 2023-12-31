from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post
from django.contrib.auth.forms import AuthenticationForm

class CustomRegistrationForm(UserCreationForm):
    school_class = forms.CharField(max_length=10, label="Klasse")
    telephone_number = forms.CharField(max_length=15, label="Telefonnummer")
    
    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = UserCreationForm.Meta.fields + ('school_class', 'telephone_number')
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Use CustomUser model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'klasse', 'content', 'image', 'deadline']
        deadline = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))