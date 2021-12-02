from django import forms 

from core.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']