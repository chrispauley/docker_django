from django import forms
from django.forms import ModelForm
from guestbook.models import GuestEntry


class GuestEntryForm(ModelForm):
    class Meta:
        model = GuestEntry
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }
