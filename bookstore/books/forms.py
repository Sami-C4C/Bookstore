from django import forms
from .models import Book
from booklists.models import Booklist


class BookForm(forms.ModelForm):



    booklists = forms.ModelMultipleChoiceField(
        queryset=Booklist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'ISBN_number', 'booklists']
