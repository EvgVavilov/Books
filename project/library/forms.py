from django import forms
from library import models


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            "name",
            "about_author",
            "slug",
            "photo",
        ]

        widgets = {
            "name": forms.TextInput(),
            "about_author": forms.Textarea(),
            "slug": forms.TextInput(),
        }

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book

        fields = [
            "name",
            "about_book",
            "slug",
            "photo",
            'link_to_shop',
            'author',
        ]

        widgets = {
            "name": forms.TextInput(),
            "about_book": forms.Textarea(),
            "slug": forms.TextInput(),
            'link_to_shop': forms.TextInput(),
            'author': forms.SelectMultiple()
        }
