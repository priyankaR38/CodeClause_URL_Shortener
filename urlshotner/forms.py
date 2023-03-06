from .models import priyanka
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=priyanka
        fields = {'original_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }
