from django import forms

from .models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)