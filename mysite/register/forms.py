from django import forms
from django.forms import ModelForm
from .models import Client


#Create a venue form
class ClientForm(ModelForm):
    class Meta:
        model =Client
        fields = "__all__"
        labels = {
            'name': 'Enter Your Name',
            'age': 'Enter Your Age',
            'phone': 'Enter Your Phone Number',
            'email': 'Enter Your Email',
            'gender': 'Enter Your Gender',
            'course': 'Enter Your Course',
        }
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            'course': forms.TextInput(attrs={'class':'form-control'}),
        }