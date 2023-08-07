from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreationForm(UserCreationForm):
    school_class = forms.CharField(max_length=10)
    telephone_number = forms.CharField(max_length=15)
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('school_class', 'telephone_number')
