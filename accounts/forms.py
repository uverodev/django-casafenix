from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image', 'document', 'first_name', 'last_name', 'region', 'city', 'phone']
        widgets = {
            'image': forms.ClearableFileInput(attrs = {'class':'form-control mt-3', }),
            'document': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'first_name': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'last_name': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'phone': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'city': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
        }
