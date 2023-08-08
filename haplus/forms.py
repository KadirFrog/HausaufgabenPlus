from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomRegistrationForm(UserCreationForm):
    school_class = forms.CharField(max_length=10)
    telephone_number = forms.CharField(max_length=15)
    
    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = UserCreationForm.Meta.fields + ('school_class', 'telephone_number')
        
class CustomAuthenticationForm(AuthenticationError):
    class Meta:
        model = CustomUser  # Use CustomUser model