from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import GameUser



class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['username', 'password']
        
class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['username', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user