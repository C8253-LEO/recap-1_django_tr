from django import forms
from django.db.models import fields
from django.forms.widgets import TextInput
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name":forms.TextInput(attrs={'placeholder':'Name'}),
            "phone_number":forms.TextInput(attrs={'placeholder':'Phone'}),
            "email":forms.EmailInput(attrs={'placeholder':'Email'}),
            "message":forms.TextInput(attrs={'placeholder':'Message'})
        }