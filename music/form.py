from django.contrib.auth.models import User
from django import forms

#Todo: Create a form inherit from USER class

class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    #TODO: Provide which fields we need
    class Meta:
        model = User
        fields = ['username', 'email', 'password']