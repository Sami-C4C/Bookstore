from django import forms
from .models import Booklist

class BooklistForm(forms.ModelForm):
    class Meta:
        model = Booklist
        fields = ['title', 'category']
